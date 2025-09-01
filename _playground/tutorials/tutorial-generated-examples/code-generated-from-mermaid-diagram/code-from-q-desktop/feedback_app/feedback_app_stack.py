from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as dynamodb,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
)
from constructs import Construct

class FeedbackAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB table
        table = dynamodb.Table(
            self, "FeedbackTable",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING)
        )

        # SNS topic
        topic = sns.Topic(self, "FeedbackTopic")
        topic.add_subscription(subscriptions.EmailSubscription("x.y@z.com"))

        # Lambda functions
        landing_page_fn = _lambda.Function(
            self, "LandingPageFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="landing_page.handler",
            code=_lambda.Code.from_asset("lambda_functions")
        )

        send_feedback_fn = _lambda.Function(
            self, "SendFeedbackFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="send_feedback.handler",
            code=_lambda.Code.from_asset("lambda_functions"),
            environment={
                "DYNAMODB_TABLE": table.table_name,
                "SNS_TOPIC_ARN": topic.topic_arn
            }
        )

        # Grant permissions
        table.grant_write_data(send_feedback_fn)
        topic.grant_publish(send_feedback_fn)

        # API Gateway
        api = apigw.RestApi(self, "FeedbackApi")

        landing_page_integration = apigw.LambdaIntegration(landing_page_fn)
        api.root.add_method("GET", landing_page_integration)

        feedback_resource = api.root.add_resource("feedbacks")
        send_feedback_integration = apigw.LambdaIntegration(send_feedback_fn)
        feedback_resource.add_method("POST", send_feedback_integration)