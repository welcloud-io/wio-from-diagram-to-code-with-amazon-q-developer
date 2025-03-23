from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    CfnOutput
)
from constructs import Construct

class SimpleLambdaBackendStack(Stack):
    """
    CDK Stack that creates an API Gateway with Mock Integration and Lambda Authorizer
    as shown in the updated architecture diagram.
    This implementation matches the lambda.drawio diagram with API Gateway connected to:
    1. A Mock Integration for handling requests
    2. A Lambda Authorizer for authorization
    """
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the Lambda Authorizer function
        authorizer_lambda = _lambda.Function(
            self, "LambdaAuthorizer",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="authorizer.handler",
            code=_lambda.Code.from_asset("../lambda"),
            description="Lambda function for API authorization"
        )
        
        # Create the API Gateway REST API
        api = apigw.RestApi(
            self, "SimpleBackendApi",
            rest_api_name="Simple Backend API",
            description="API Gateway with Mock Integration and Lambda Authorizer",
            deploy_options=apigw.StageOptions(
                stage_name="prod",
                throttling_rate_limit=100,
                throttling_burst_limit=50
            ),
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=["GET", "POST", "OPTIONS"],
                allow_headers=["Content-Type", "X-Amz-Date", "Authorization", "X-Api-Key", "X-Amz-Security-Token"]
            )
        )
        
        # Create the Lambda Authorizer
        lambda_authorizer = apigw.TokenAuthorizer(
            self, "ApiAuthorizer",
            handler=authorizer_lambda,
            results_cache_ttl=None  # Disable caching for testing
        )
        
        # Add a resource and method with Mock Integration
        resource = api.root.add_resource("api")
        
        # Add GET method with Mock Integration and Lambda Authorizer
        get_integration = apigw.MockIntegration(
            integration_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Origin': "'*'",
                },
                'responseTemplates': {
                    'application/json': '{"message": "This is a mock response for GET"}'
                }
            }],
            request_templates={
                'application/json': '{"statusCode": 200}'
            }
        )
        
        resource.add_method('GET', get_integration,
            method_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Origin': True,
                }
            }],
            authorizer=lambda_authorizer
        )
        
        # Add POST method with Mock Integration and Lambda Authorizer
        post_integration = apigw.MockIntegration(
            integration_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Origin': "'*'",
                },
                'responseTemplates': {
                    'application/json': '{"message": "This is a mock response for POST"}'
                }
            }],
            request_templates={
                'application/json': '{"statusCode": 200}'
            }
        )
        
        resource.add_method('POST', post_integration,
            method_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Origin': True,
                }
            }],
            authorizer=lambda_authorizer
        )
        
        # Output the API Gateway URL
        CfnOutput(
            self, "ApiUrl",
            value=f"{api.url}api",
            description="URL of the API Gateway"
        )