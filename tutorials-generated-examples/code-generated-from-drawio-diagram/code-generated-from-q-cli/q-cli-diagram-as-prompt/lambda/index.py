import json

def handler(event, context):
    """
    Lambda function handler that processes API Gateway requests.
    
    Args:
        event (dict): Event data from API Gateway
        context (object): Lambda context object
        
    Returns:
        dict: API Gateway response object
    """
    try:
        # Log the incoming event for debugging
        print(f"Received event: {json.dumps(event)}")
        
        # Extract HTTP method and path from the event
        http_method = event.get('httpMethod', '')
        path = event.get('path', '')
        
        # Process based on HTTP method and path
        if http_method == 'GET':
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'  # For CORS support
                },
                'body': json.dumps({
                    'message': 'Hello from Lambda!',
                    'path': path
                })
            }
        elif http_method == 'POST':
            # Parse the request body
            body = json.loads(event.get('body', '{}'))
            
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'  # For CORS support
                },
                'body': json.dumps({
                    'message': 'Data received successfully',
                    'data': body
                })
            }
        else:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'  # For CORS support
                },
                'body': json.dumps({
                    'message': f'Unsupported method: {http_method}'
                })
            }
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # For CORS support
            },
            'body': json.dumps({
                'message': 'Internal server error'
            })
        }