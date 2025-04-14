def handler(event, context):
    """
    Lambda function that performs 1+1 addition
    """
    result = 1 + 1
    return {
        'statusCode': 200,
        'body': {
            'result': result
        }
    }