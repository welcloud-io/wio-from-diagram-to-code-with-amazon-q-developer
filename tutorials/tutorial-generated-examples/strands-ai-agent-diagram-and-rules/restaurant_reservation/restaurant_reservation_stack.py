from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    RemovalPolicy,
    Duration
)
from constructs import Construct

class RestaurantReservationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB Table for reservations
        reservation_table = dynamodb.Table(
            self, "RestaurantReservationTable",
            table_name="restaurant-reservations",
            partition_key=dynamodb.Attribute(
                name="reservation_id",
                type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY
        )

        # Lambda Layer for Strands
        strands_layer = _lambda.LayerVersion(
            self, "StrandsLayer",
            code=_lambda.Code.from_asset("layers/strands"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_10],
            description="Strands agents and tools"
        )

        # AI Agent Lambda
        ai_agent_lambda = _lambda.Function(
            self, "RestaurantReservationAIAgent",
            function_name="restaurant-reservation-ai-agent",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/ai_agent"),
            layers=[strands_layer],
            timeout=Duration.seconds(30),
            environment={
                "TABLE_NAME": reservation_table.table_name
            }
        )

        # Landing Page Lambda
        landing_page_lambda = _lambda.Function(
            self, "ConversationLandingPage",
            function_name="conversation-landing-page",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/landing_page"),
            timeout=Duration.seconds(10)
        )

        # Grant permissions
        reservation_table.grant_read_write_data(ai_agent_lambda)
        
        ai_agent_lambda.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
                resources=["arn:aws:bedrock:*::foundation-model/anthropic.claude-3-haiku-20240307-v1:0"]
            )
        )

        # API Gateway
        api = apigw.RestApi(
            self, "RestaurantReservationAPI",
            rest_api_name="Restaurant Reservation Service"
        )

        # API Gateway integrations
        ai_agent_integration = apigw.LambdaIntegration(ai_agent_lambda)
        landing_page_integration = apigw.LambdaIntegration(landing_page_lambda)

        # API routes
        api.root.add_method("GET", landing_page_integration)
        
        chat_resource = api.root.add_resource("chat")
        chat_resource.add_method("POST", ai_agent_integration)