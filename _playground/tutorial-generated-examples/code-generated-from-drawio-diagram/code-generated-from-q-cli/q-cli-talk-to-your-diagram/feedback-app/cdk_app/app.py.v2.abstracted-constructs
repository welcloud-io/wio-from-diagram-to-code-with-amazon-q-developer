#!/usr/bin/env python3
import os
from aws_cdk import (
    App,
    Stack,
    Duration,
    RemovalPolicy,
    CfnOutput,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as dynamodb,
    aws_sns as sns,
    aws_sns_subscriptions as sns_subs,
    aws_iam as iam,
)
from constructs import Construct

class FeedbackApiGateway(Construct):
    """
    Construct for the API Gateway component of the Feedback application.
    Creates API endpoints for the landing page and feedback submission.
    """
    def __init__(self, scope: Construct, id: str, landing_page_lambda: _lambda.Function, record_feedback_lambda: _lambda.Function):
        super().__init__(scope, id)
        
        # Create API Gateway
        self.api = apigw.RestApi(
            self, "FeedbackApi",
            rest_api_name="Feedback Service",
            description="API for submitting and managing feedback"
        )
        
        # Create API resources and methods
        landing_page_resource = self.api.root.add_resource("landing")
        landing_page_integration = apigw.LambdaIntegration(landing_page_lambda)
        landing_page_resource.add_method("GET", landing_page_integration)
        
        feedback_resource = self.api.root.add_resource("feedback")
        feedback_integration = apigw.LambdaIntegration(record_feedback_lambda)
        feedback_resource.add_method("POST", feedback_integration)


class FeedbackLambdaFunctions(Construct):
    """
    Construct for the Lambda functions of the Feedback application.
    Creates and configures the landing page and record feedback functions.
    """
    def __init__(self, scope: Construct, id: str, feedback_table: dynamodb.Table, feedback_topic: sns.Topic):
        super().__init__(scope, id)
        
        # Create Lambda function for landing page
        self.landing_page_function = _lambda.Function(
            self, "LandingPageFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="landing_page.handler",
            code=_lambda.Code.from_asset("lambda_functions"),
            timeout=Duration.seconds(30),
        )
        
        # Create Lambda function for recording and confirming feedback
        self.record_feedback_function = _lambda.Function(
            self, "RecordFeedbackFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="record_feedback.handler",
            code=_lambda.Code.from_asset("lambda_functions"),
            timeout=Duration.seconds(30),
            environment={
                "FEEDBACK_TABLE_NAME": feedback_table.table_name,
                "FEEDBACK_TOPIC_ARN": feedback_topic.topic_arn,
            }
        )
        
        # Grant permissions to Lambda functions
        feedback_table.grant_read_write_data(self.record_feedback_function)
        feedback_topic.grant_publish(self.record_feedback_function)


class FeedbackTable(Construct):
    """
    Construct for the DynamoDB table of the Feedback application.
    Creates a table for storing feedback submissions.
    """
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        
        # Create DynamoDB table for feedback
        self.table = dynamodb.Table(
            self, "FeedbackTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY,  # For demo purposes only
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )


class FeedbackNotification(Construct):
    """
    Construct for the notification system of the Feedback application.
    Creates an SNS topic and email subscription for feedback notifications.
    """
    def __init__(self, scope: Construct, id: str, email_address: str):
        super().__init__(scope, id)
        
        # Create SNS Topic for feedback notifications
        self.topic = sns.Topic(
            self, "FeedbackTopic",
            display_name="Feedback Notifications"
        )
        
        # Add email subscription to the SNS topic
        self.topic.add_subscription(
            sns_subs.EmailSubscription(email_address)
        )


class FeedbackAppStack(Stack):
    """
    Main stack for the Feedback application.
    Composes all the constructs together to form the complete application.
    """
    def __init__(self, scope: Construct, construct_id: str, email_address: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create the database construct
        feedback_db = FeedbackTable(self, "FeedbackDatabase")
        
        # Create the notification construct
        notifications = FeedbackNotification(self, "FeedbackNotifications", email_address)
        
        # Create the Lambda functions construct
        lambda_functions = FeedbackLambdaFunctions(
            self, "FeedbackFunctions",
            feedback_table=feedback_db.table,
            feedback_topic=notifications.topic
        )
        
        # Create the API Gateway construct
        api_gateway = FeedbackApiGateway(
            self, "FeedbackApi",
            landing_page_lambda=lambda_functions.landing_page_function,
            record_feedback_lambda=lambda_functions.record_feedback_function
        )
        
        # Output the API Gateway URL
        CfnOutput(
            self, "ApiUrl",
            value=f"{api_gateway.api.url}landing",
            description="URL for the landing page"
        )


# Application entry point
app = App()
FeedbackAppStack(
    app, "FeedbackAppStack",
    email_address="your-email@example.com"  # Replace with your email
)
app.synth()