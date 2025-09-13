import json
import pytest
import boto3
from moto import mock_dynamodb
from lambdas.ai_agent.lambda_function import lambda_handler

@mock_dynamodb
def test_ai_agent_lambda():
    # Create mock DynamoDB table
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
        TableName='restaurant-reservations',
        KeySchema=[{'AttributeName': 'reservation_id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'reservation_id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    
    # Test event
    event = {
        'body': json.dumps({'message': 'I want to make a reservation'})
    }
    
    # Mock environment
    import os
    os.environ['TABLE_NAME'] = 'restaurant-reservations'
    
    # Call lambda
    response = lambda_handler(event, None)
    
    # Assertions
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert 'response' in body