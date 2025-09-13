import json
import os
import boto3
from strands import Agent, tool
from strands_tools import current_time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

@tool
def create_reservation(customer_name: str, date: str, time: str, party_size: int, phone: str) -> str:
    """Create a restaurant reservation"""
    import uuid
    
    reservation_id = str(uuid.uuid4())
    
    table.put_item(
        Item={
            'reservation_id': reservation_id,
            'customer_name': customer_name,
            'date': date,
            'time': time,
            'party_size': party_size,
            'phone': phone,
            'status': 'confirmed'
        }
    )
    
    return f"Reservation created successfully! ID: {reservation_id}"

@tool
def check_availability(date: str, time: str) -> str:
    """Check table availability for a specific date and time"""
    # Simple availability check - in real app would check against existing reservations
    return f"Tables are available for {date} at {time}"

@tool
def cancel_reservation(reservation_id: str) -> str:
    """Cancel an existing reservation"""
    try:
        table.delete_item(Key={'reservation_id': reservation_id})
        return f"Reservation {reservation_id} has been cancelled"
    except Exception as e:
        return f"Error cancelling reservation: {str(e)}"

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_message = body.get('message', '')
        
        system_prompt = """You are a helpful restaurant reservation assistant. You can help customers:
        - Make new reservations
        - Check table availability  
        - Cancel existing reservations
        
        Always be polite and ask for required information: customer name, date, time, party size, and phone number for new reservations."""
        
        agent = Agent(
            model="anthropic.claude-3-haiku-20240307-v1:0",
            tools=[create_reservation, check_availability, cancel_reservation, current_time],
            system_prompt=system_prompt
        )
        
        response = agent(user_message)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'response': str(response)})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }