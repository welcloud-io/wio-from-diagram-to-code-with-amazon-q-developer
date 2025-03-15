import json
import os
import uuid
import boto3
from datetime import datetime

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Get environment variables
FEEDBACK_TABLE_NAME = os.environ.get('FEEDBACK_TABLE_NAME')
FEEDBACK_TOPIC_ARN = os.environ.get('FEEDBACK_TOPIC_ARN')

# Initialize DynamoDB table
feedback_table = dynamodb.Table(FEEDBACK_TABLE_NAME)

def handler(event, context):
    """
    Lambda function that records feedback in DynamoDB and sends a confirmation email via SNS.
    
    This function processes the feedback form submission, stores the data in DynamoDB,
    and sends a confirmation notification via SNS.
    """
    try:
        # Parse the request body
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Invalid request format'})
            }
        
        # Extract feedback data
        name = body.get('name', '')
        email = body.get('email', '')
        feedback_text = body.get('feedback', '')
        rating = int(body.get('rating', 0))
        
        # Validate required fields
        if not all([name, email, feedback_text, rating]):
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Missing required fields'})
            }
        
        # Generate a unique ID for the feedback
        feedback_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        # Create feedback item
        feedback_item = {
            'id': feedback_id,
            'name': name,
            'email': email,
            'feedback': feedback_text,
            'rating': rating,
            'timestamp': timestamp
        }
        
        # Store feedback in DynamoDB
        feedback_table.put_item(Item=feedback_item)
        
        # Prepare SNS message
        sns_message = f"""
        New Feedback Received:
        
        Name: {name}
        Email: {email}
        Rating: {rating}/5
        Timestamp: {timestamp}
        
        Feedback:
        {feedback_text}
        
        Feedback ID: {feedback_id}
        """
        
        # Send SNS notification
        sns.publish(
            TopicArn=FEEDBACK_TOPIC_ARN,
            Subject=f"New Feedback from {name}",
            Message=sns_message
        )
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Thank you for your feedback! We have sent a confirmation to your email.',
                'feedbackId': feedback_id
            })
        }
        
    except Exception as e:
        print(f"Error processing feedback: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'An error occurred processing your feedback'})
        }