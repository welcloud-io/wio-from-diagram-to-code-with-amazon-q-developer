def handler(event, context):
    # Simple addition 1+1
    result = 1 + 1
    return {
        'statusCode': 200,
        'result': result
    }