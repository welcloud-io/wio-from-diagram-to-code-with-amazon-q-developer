def handler(event, context):
    """
    Lambda function that performs 3+3 addition
    """
    result = 3 + 3
    return {
        'statusCode': 200,
        'body': {
            'result': result
        }
    }