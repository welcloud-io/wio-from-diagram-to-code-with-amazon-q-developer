landing_page = open('index.html').read()

def lambda_handler(event, context):
    return {
    "statusCode": 200,
    "body": landing_page,
    "headers": {
        'Content-Type': 'text/html',
    }
}