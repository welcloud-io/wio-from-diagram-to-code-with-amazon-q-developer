import json
import os
import boto3
from datetime import datetime
import uuid

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

def handler(event, context):
    """
    Record and Confirm Lambda function that:
    1. Receives feedback from API Gateway
    2. Stores it in DynamoDB
    3. Publishes confirmation to SNS
    """
    try:
        # Parse the incoming request body
        body = json.loads(event['body'])
        
        # Get environment variables
        table_name = os.environ['FEEDBACK_TABLE_NAME']
        sns_topic_arn = os.environ['SNS_TOPIC_ARN']
        
        # Create a unique ID for the feedback
        feedback_id = str(uuid.uuid4())
        
        # Prepare the item for DynamoDB
        feedback_item = {
            'id': feedback_id,
            'name': body['name'],
            'email': body['email'],
            'feedback': body['feedback'],
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Store in DynamoDB
        table = dynamodb.Table(table_name)
        table.put_item(Item=feedback_item)
        
        # Publish to SNS
        sns_message = {
            'feedback_id': feedback_id,
            'name': body['name'],
            'email': body['email']
        }
        
        sns.publish(
            TopicArn=sns_topic_arn,
            Message=json.dumps(sns_message),
            Subject='New Feedback Received'
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Feedback submitted successfully',
                'feedback_id': feedback_id
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Error processing feedback'
            })
        }