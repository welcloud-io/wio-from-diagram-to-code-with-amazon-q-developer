from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_kms as kms,
    aws_lambda as lambda_,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
    aws_events as events,
    aws_events_targets as targets,
    Duration,
    RemovalPolicy
)
from constructs import Construct

class CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create KMS key for S3 bucket encryption
        kms_key = kms.Key(self, "BucketKey",
            enable_key_rotation=True,
            alias="custom-s3-key",
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create S3 bucket with versioning and encryption
        bucket = s3.Bucket(self, "VersionedBucket",
            versioned=True,
            encryption=s3.BucketEncryption.KMS,
            encryption_key=kms_key,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            event_bridge_enabled=True
        )

        # Create Lambda functions
        lambda1 = lambda_.Function(self, "Lambda1",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/lambda1"),
            timeout=Duration.seconds(30)
        )

        lambda2 = lambda_.Function(self, "Lambda2",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/lambda2"),
            timeout=Duration.seconds(30)
        )

        lambda3 = lambda_.Function(self, "Lambda3",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/lambda3"),
            timeout=Duration.seconds(30)
        )

        # Create Step Functions tasks
        task1 = tasks.LambdaInvoke(self, "Task1",
            lambda_function=lambda1,
            output_path="$.Payload"
        )

        task2 = tasks.LambdaInvoke(self, "Task2",
            lambda_function=lambda2,
            output_path="$.Payload"
        )

        task3 = tasks.LambdaInvoke(self, "Task3",
            lambda_function=lambda3,
            output_path="$.Payload"
        )

        # Create parallel state for task2 and task3
        parallel_state = sfn.Parallel(self, "ParallelExecution")
        parallel_state.branch(task2)
        parallel_state.branch(task3)

        # Create Step Functions state machine
        definition = task1.next(parallel_state)

        state_machine = sfn.StateMachine(self, "StateMachine",
            definition=definition,
            timeout=Duration.minutes(5)
        )

        # Create EventBridge rule
        rule = events.Rule(self, "S3EventRule",
            event_pattern=events.EventPattern(
                source=["aws.s3"],
                detail_type=["Object Created"],
                detail={
                    "bucket": {
                        "name": [bucket.bucket_name]
                    },
                    "object": {
                        "key": [{
                            "prefix": ""  # Match all objects
                        }]
                    }
                }
            )
        )

        # Add Step Functions state machine as target
        rule.add_target(targets.SfnStateMachine(state_machine))