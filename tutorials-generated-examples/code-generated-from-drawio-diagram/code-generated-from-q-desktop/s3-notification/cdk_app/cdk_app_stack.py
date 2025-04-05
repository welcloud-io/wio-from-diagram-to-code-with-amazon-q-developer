from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as lambda_,
    aws_s3_notifications as s3n,
    aws_iam as iam,
    Duration,
    RemovalPolicy
)
from constructs import Construct

class CdkAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket
        bucket = s3.Bucket(
            self, "FileProcessingBucket",
            removal_policy=RemovalPolicy.DESTROY,  # For development only
            auto_delete_objects=True  # For development only
        )

        # Create Lambda function
        processor_lambda = lambda_.Function(
            self, "FileProcessorFunction",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="handler.handler",
            code=lambda_.Code.from_asset("cdk_app/lambda"),
            timeout=Duration.minutes(5),
            environment={
                "THIRD_PARTY_API_KEY": "xxx",
                "THIRD_PARTY_ENDPOINT": "https://third-party-provider.com/api"  # Replace with actual endpoint
            }
        )

        # Grant Lambda permissions to read from S3
        bucket.grant_read(processor_lambda)

        # Add S3 notification to trigger Lambda
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(processor_lambda)
        )

        # Add permissions for Lambda to call third-party API
        processor_lambda.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["secretsmanager:GetSecretValue"],
                resources=["*"]  # Scope this down to specific secret ARN in production
            )
        )

