import json
import os
import boto3
import requests
from botocore.exceptions import ClientError

def handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    try:
        # Get bucket and file details from the event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Download file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        file_content = response['Body'].read()
        
        # Get third-party API credentials
        third_party_api_key = os.environ['THIRD_PARTY_API_KEY']
        third_party_endpoint = os.environ['THIRD_PARTY_ENDPOINT']
        
        # Process file and send to third-party provider
        headers = {
            'Authorization': f'Bearer {third_party_api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'filename': key,
            'content': file_content.decode('utf-8')  # Adjust encoding as needed
        }
        
        # Send to third-party provider
        response = requests.post(
            third_party_endpoint,
            headers=headers,
            json=payload
        )
        
        response.raise_for_status()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File processed successfully',
                'filename': key
            })
        }
        
    except ClientError as e:
        print(f"Error accessing S3: {str(e)}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Error calling third-party API: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise
