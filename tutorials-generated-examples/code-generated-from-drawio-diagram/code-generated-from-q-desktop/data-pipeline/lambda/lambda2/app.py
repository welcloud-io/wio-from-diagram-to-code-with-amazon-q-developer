def handler(event, context):
    """
    Lambda function that performs 2+2 addition
    """
    result = 2 + 2
    return {
        'statusCode': 200,
        'body': {
            'result': result
        }
    }