#!/usr/bin/env python3
import os
import aws_cdk as cdk
from serverless_web_app.serverless_web_app_stack import ServerlessWebAppStack

app = cdk.App()
ServerlessWebAppStack(app, "ServerlessWebAppStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
    )
)

app.synth()
