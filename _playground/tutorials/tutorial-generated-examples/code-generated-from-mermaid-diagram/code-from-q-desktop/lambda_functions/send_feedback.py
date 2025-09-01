import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

sns = boto3.client('sns')
topic_arn = os.environ['SNS_TOPIC_ARN']

def handler(event, context):
    try:
        # Parse the incoming request body
        body = json.loads(event['body'])
        feedback = body['feedback']
        
        # Store feedback in DynamoDB
        table.put_item(Item={'id': context.aws_request_id, 'feedback': feedback})
        
        # Publish feedback to SNS topic
        sns.publish(
            TopicArn=topic_arn,
            Subject='New Feedback Received',
            Message=f'New feedback: {feedback}'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Feedback submitted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }