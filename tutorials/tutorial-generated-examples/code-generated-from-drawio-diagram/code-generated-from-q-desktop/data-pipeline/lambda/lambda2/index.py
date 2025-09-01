def handler(event, context):
    # Simple addition 2+2
    result = 2 + 2
    return {
        'statusCode': 200,
        'result': result
    }