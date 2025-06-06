from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_logs as logs,
    Duration,
    CfnOutput
)
from constructs import Construct

class ServerlessWebAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda function for landing page
        landing_page_lambda = _lambda.Function(
            self, "LandingPageFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("lambda"),
            handler="landing_page.handler",
            timeout=Duration.seconds(30),
            memory_size=128,
            description="Lambda function to serve the landing page",
            log_retention=logs.RetentionDays.ONE_WEEK
        )

        # Create API Gateway
        api = apigateway.RestApi(
            self, "ServerlessWebAppApi",
            rest_api_name="Serverless Web App API",
            description="API Gateway for the serverless web application",
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=["Content-Type", "X-Amz-Date", "Authorization", "X-Api-Key"]
            ),
            deploy_options=apigateway.StageOptions(
                stage_name="prod",
                throttling_rate_limit=100,
                throttling_burst_limit=200
            )
        )

        # Create Lambda integration
        landing_page_integration = apigateway.LambdaIntegration(
            landing_page_lambda,
            request_templates={"application/json": '{ "statusCode": "200" }'}
        )

        # Add GET method to root resource for landing page
        api.root.add_method("GET", landing_page_integration)

        # Add a catch-all proxy resource for SPA routing
        proxy_resource = api.root.add_resource("{proxy+}")
        proxy_resource.add_method("GET", landing_page_integration)

        # Output the API Gateway URL
        CfnOutput(
            self, "ApiGatewayUrl",
            value=api.url,
            description="URL of the API Gateway"
        )

        # Output the Lambda function name
        CfnOutput(
            self, "LandingPageFunctionName",
            value=landing_page_lambda.function_name,
            description="Name of the Landing Page Lambda function"
        )
