import json
import re

def handler(event, context):
    """
    Lambda Authorizer function for API Gateway.
    
    Args:
        event (dict): Event data from API Gateway
        context (object): Lambda context object
        
    Returns:
        dict: IAM policy document
    """
    try:
        # Log the incoming event for debugging
        print(f"Received authorization event: {json.dumps(event)}")
        
        # Get the authorization token from the request
        token = event.get('authorizationToken', '')
        
        # Check if the token is valid (in a real scenario, you would validate against a proper auth system)
        # For this example, we'll accept tokens that start with "Bearer " and contain "allow"
        is_authorized = bool(re.match(r'^Bearer .*allow.*$', token, re.IGNORECASE))
        
        # Get the method ARN from the event
        method_arn = event.get('methodArn', '')
        
        # Create the IAM policy document based on authorization result
        if is_authorized:
            return generate_policy('user', 'Allow', method_arn)
        else:
            return generate_policy('user', 'Deny', method_arn)
            
    except Exception as e:
        print(f"Error in authorizer: {str(e)}")
        # In case of error, deny access
        return generate_policy('user', 'Deny', event.get('methodArn', ''))

def generate_policy(principal_id, effect, resource):
    """
    Generate an IAM policy document.
    
    Args:
        principal_id (str): Principal ID (user identifier)
        effect (str): Allow or Deny
        resource (str): Resource ARN
        
    Returns:
        dict: Policy document
    """
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                }
            ]
        },
        # Additional context information that can be used in the API
        'context': {
            'stringKey': 'string value',
            'numberKey': 123,
            'booleanKey': True
        }
    }