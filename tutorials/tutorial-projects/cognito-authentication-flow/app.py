#!/usr/bin/env python3
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

class WebAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Login Lambda Function
        login_function = _lambda.Function(
            self, "LoginFunction",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="login.handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Protected Page Lambda Function
        protected_function = _lambda.Function(
            self, "ProtectedFunction",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="protected.handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # API Gateway
        api = apigw.RestApi(self, "WebAppApi")
        
        # Routes
        api.root.add_resource("login").add_method("GET", apigw.LambdaIntegration(login_function))
        api.root.add_resource("protected").add_method("GET", apigw.LambdaIntegration(protected_function))

app = cdk.App()
WebAppStack(app, "WebAppStack")
app.synth()