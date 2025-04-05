import json
import os
import unittest
from unittest.mock import patch, MagicMock

import boto3
import requests
from botocore.exceptions import ClientError

# Import the handler function
import sys
sys.path.append('cdk_app/lambda')
from handler import handler

class TestLambdaHandler(unittest.TestCase):
    
    @patch('handler.boto3.client')
    @patch('handler.requests.post')
    def test_successful_processing(self, mock_requests_post, mock_boto3_client):
        # Setup mock S3 client
        mock_s3 = MagicMock()
        mock_boto3_client.return_value = mock_s3
        
        # Mock S3 get_object response
        mock_s3.get_object.return_value = {
            'Body': MagicMock(read=lambda: b'test file content')
        }
        
        # Mock requests.post response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_requests_post.return_value = mock_response
        
        # Setup environment variables
        os.environ['THIRD_PARTY_API_KEY'] = 'test-api-key'
        os.environ['THIRD_PARTY_ENDPOINT'] = 'https://test-endpoint.com'
        
        # Create test event
        event = {
            'Records': [
                {
                    's3': {
                        'bucket': {
                            'name': 'test-bucket'
                        },
                        'object': {
                            'key': 'test-file.txt'
                        }
                    }
                }
            ]
        }
        
        # Call the handler
        response = handler(event, {})
        
        # Assertions
        mock_s3.get_object.assert_called_once_with(Bucket='test-bucket', Key='test-file.txt')
        
        mock_requests_post.assert_called_once()
        args, kwargs = mock_requests_post.call_args
        self.assertEqual(args[0], 'https://test-endpoint.com')
        self.assertEqual(kwargs['headers']['Authorization'], 'Bearer test-api-key')
        self.assertEqual(kwargs['json']['filename'], 'test-file.txt')
        self.assertEqual(kwargs['json']['content'], 'test file content')
        
        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['message'], 'File processed successfully')
        self.assertEqual(body['filename'], 'test-file.txt')
    
    @patch('handler.boto3.client')
    def test_s3_client_error(self, mock_boto3_client):
        # Setup mock S3 client to raise ClientError
        mock_s3 = MagicMock()
        mock_boto3_client.return_value = mock_s3
        
        error_response = {'Error': {'Code': 'NoSuchKey', 'Message': 'The specified key does not exist.'}}
        mock_s3.get_object.side_effect = ClientError(error_response, 'GetObject')
        
        # Create test event
        event = {
            'Records': [
                {
                    's3': {
                        'bucket': {
                            'name': 'test-bucket'
                        },
                        'object': {
                            'key': 'non-existent-file.txt'
                        }
                    }
                }
            ]
        }
        
        # Call the handler and expect exception
        with self.assertRaises(ClientError):
            handler(event, {})
    
    @patch('handler.boto3.client')
    @patch('handler.requests.post')
    def test_api_request_error(self, mock_requests_post, mock_boto3_client):
        # Setup mock S3 client
        mock_s3 = MagicMock()
        mock_boto3_client.return_value = mock_s3
        
        # Mock S3 get_object response
        mock_s3.get_object.return_value = {
            'Body': MagicMock(read=lambda: b'test file content')
        }
        
        # Mock requests.post to raise exception
        mock_requests_post.side_effect = requests.exceptions.RequestException("API Error")
        
        # Setup environment variables
        os.environ['THIRD_PARTY_API_KEY'] = 'test-api-key'
        os.environ['THIRD_PARTY_ENDPOINT'] = 'https://test-endpoint.com'
        
        # Create test event
        event = {
            'Records': [
                {
                    's3': {
                        'bucket': {
                            'name': 'test-bucket'
                        },
                        'object': {
                            'key': 'test-file.txt'
                        }
                    }
                }
            ]
        }
        
        # Call the handler and expect exception
        with self.assertRaises(requests.exceptions.RequestException):
            handler(event, {})

if __name__ == '__main__':
    unittest.main()
