import aws_cdk as cdk
import aws_cdk.assertions as assertions
from lib.simple_lambda_backend_stack import SimpleLambdaBackendStack

def test_api_gateway_created():
    """Test that the API Gateway is created with the correct configuration."""
    # ARRANGE
    app = cdk.App()
    
    # ACT
    stack = SimpleLambdaBackendStack(app, "TestStack")
    template = assertions.Template.from_stack(stack)
    
    # ASSERT
    # Check that the API Gateway REST API is created
    template.resource_count_is("AWS::ApiGateway::RestApi", 1)
    
    # Check that the API Gateway has a deployment and stage
    template.resource_count_is("AWS::ApiGateway::Deployment", 1)
    template.resource_count_is("AWS::ApiGateway::Stage", 1)
    
    # Check that the stage is named 'prod'
    template.has_resource_properties(
        "AWS::ApiGateway::Stage",
        {
            "StageName": "prod"
        }
    )

def test_lambda_authorizer_created():
    """Test that the Lambda Authorizer is created with the correct configuration."""
    # ARRANGE
    app = cdk.App()
    
    # ACT
    stack = SimpleLambdaBackendStack(app, "TestStack")
    template = assertions.Template.from_stack(stack)
    
    # ASSERT
    # Check that the Lambda function is created
    template.resource_count_is("AWS::Lambda::Function", 1)
    
    # Check that the Lambda function has the correct runtime and handler
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "authorizer.handler",
            "Runtime": "python3.9"
        }
    )
    
    # Check that the API Gateway Authorizer is created
    template.resource_count_is("AWS::ApiGateway::Authorizer", 1)
    
    # Check that the Authorizer is of type TOKEN
    template.has_resource_properties(
        "AWS::ApiGateway::Authorizer",
        {
            "Type": "TOKEN"
        }
    )

def test_api_methods_created():
    """Test that the API Gateway methods are created with the correct configuration."""
    # ARRANGE
    app = cdk.App()
    
    # ACT
    stack = SimpleLambdaBackendStack(app, "TestStack")
    template = assertions.Template.from_stack(stack)
    
    # ASSERT
    # Check that the API Gateway methods are created
    # We expect 4 methods: GET, POST, OPTIONS (for CORS), and OPTIONS for the resource
    template.resource_count_is("AWS::ApiGateway::Method", 4)
    
    # Check that the GET method has the correct integration type (MOCK)
    template.has_resource_properties(
        "AWS::ApiGateway::Method",
        {
            "HttpMethod": "GET",
            "Integration": {
                "Type": "MOCK"
            },
            "AuthorizationType": "CUSTOM"
        }
    )
    
    # Check that the POST method has the correct integration type (MOCK)
    template.has_resource_properties(
        "AWS::ApiGateway::Method",
        {
            "HttpMethod": "POST",
            "Integration": {
                "Type": "MOCK"
            },
            "AuthorizationType": "CUSTOM"
        }
    )

def test_cors_configuration():
    """Test that CORS is properly configured."""
    # ARRANGE
    app = cdk.App()
    
    # ACT
    stack = SimpleLambdaBackendStack(app, "TestStack")
    template = assertions.Template.from_stack(stack)
    
    # ASSERT
    # Check that the OPTIONS method exists for CORS
    template.has_resource_properties(
        "AWS::ApiGateway::Method",
        {
            "HttpMethod": "OPTIONS",
            "Integration": {
                "Type": "MOCK"
            },
            "AuthorizationType": "NONE"  # OPTIONS should not require authorization
        }
    )
    
    # Check that the GET method has the correct CORS headers
    template.has_resource_properties(
        "AWS::ApiGateway::Method",
        {
            "HttpMethod": "GET",
            "MethodResponses": [
                {
                    "ResponseParameters": {
                        "method.response.header.Access-Control-Allow-Origin": True
                    }
                }
            ]
        }
    )

def test_outputs_created():
    """Test that the expected CloudFormation outputs are created."""
    # ARRANGE
    app = cdk.App()
    
    # ACT
    stack = SimpleLambdaBackendStack(app, "TestStack")
    template = assertions.Template.from_stack(stack)
    
    # ASSERT
    # Check that the API URL output is created
    template.has_output("ApiUrl", {})