#!/usr/bin/env python3

import aws_cdk as cdk
from lib.simple_lambda_backend_stack import SimpleLambdaBackendStack

app = cdk.App()

# Create the main stack
SimpleLambdaBackendStack(app, "SimpleLambdaBackendStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    #
    # env=cdk.Environment(account='123456789012', region='us-east-1'),
    
    # Uncomment the line below to specify your AWS account and region
    # env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)

app.synth()