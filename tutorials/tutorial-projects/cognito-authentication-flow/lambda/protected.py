import json

def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '''
        <html>
        <body>
            <h1>Protected Page</h1>
            <p>Welcome! You have access to this protected content.</p>
        </body>
        </html>
        '''
    }