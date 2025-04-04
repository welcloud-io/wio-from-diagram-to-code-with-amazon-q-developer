from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_apigateway as apigw,
    RemovalPolicy,
)

class FeedbackStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create DynamoDB table
        feedback_table = dynamodb.Table(
            self, "FeedbackTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY,  # For demo purposes only
            point_in_time_recovery=True
        )

        # Create SNS Topic
        feedback_topic = sns.Topic(
            self, "FeedbackTopic",
            display_name="Feedback Notifications"
        )

        # Add email subscription to SNS topic
        feedback_topic.add_subscription(
            subscriptions.EmailSubscription("your-email@example.com")  # Replace with your email
        )

        # Create Lambda functions
        landing_page_fn = _lambda.Function(
            self, "LandingPageFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="app.handler",
            code=_lambda.Code.from_asset("lambda/landing_page")
        )

        record_confirm_fn = _lambda.Function(
            self, "RecordConfirmFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="app.handler",
            code=_lambda.Code.from_asset("lambda/record_confirm"),
            environment={
                "FEEDBACK_TABLE_NAME": feedback_table.table_name,
                "SNS_TOPIC_ARN": feedback_topic.topic_arn
            }
        )

        # Grant permissions
        feedback_table.grant_write_data(record_confirm_fn)
        feedback_topic.grant_publish(record_confirm_fn)

        # Create API Gateway
        api = apigw.RestApi(
            self, "FeedbackApi",
            rest_api_name="Feedback Service",
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=["*"],
                allow_methods=["GET", "POST"],
                allow_headers=["Content-Type"]
            )
        )

        # Add routes
        api.root.add_method(
            "GET",
            apigw.LambdaIntegration(landing_page_fn)
        )

        feedback_resource = api.root.add_resource("submit-feedback")
        feedback_resource.add_method(
            "POST",
            apigw.LambdaIntegration(record_confirm_fn)
        )