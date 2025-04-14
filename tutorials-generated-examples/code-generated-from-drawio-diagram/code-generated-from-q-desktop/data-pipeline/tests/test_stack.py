import aws_cdk as cdk
from aws_cdk.assertions import Template
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cdk.stacks.main_stack import MainStack

def test_stack_resources():
    app = cdk.App()
    stack = MainStack(app, "TestStack")
    template = Template.from_stack(stack)

    # Verify S3 bucket with versioning
    template.has_resource_properties("AWS::S3::Bucket", {
        "VersioningConfiguration": {
            "Status": "Enabled"
        }
    })

    # Verify KMS key
    template.has_resource_properties("AWS::KMS::Key", {
        "EnableKeyRotation": True
    })

    # Verify Lambda functions
    template.resource_count_is("AWS::Lambda::Function", 3)

    # Verify Step Functions state machine
    template.has_resource("AWS::StepFunctions::StateMachine")

    # Verify EventBridge rule
    template.has_resource("AWS::Events::Rule")