def handler(event, context):
    # Simple addition 3+3
    result = 3 + 3
    return {
        'statusCode': 200,
        'result': result
    }