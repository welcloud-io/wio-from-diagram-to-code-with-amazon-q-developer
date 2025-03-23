import pytest
import os
import json
import boto3
import requests
from unittest import mock

# This test requires the stack to be deployed
# It will be skipped if the API_URL environment variable is not set
# To run this test: API_URL=<your-api-url> pytest tests/test_integration.py

@pytest.mark.skipif("API_URL" not in os.environ, reason="API_URL environment variable not set")
class TestIntegration:
    """Integration tests for the deployed API."""
    
    @classmethod
    def setup_class(cls):
        """Set up the test class."""
        cls.api_url = os.environ.get("API_URL")
        if not cls.api_url.endswith("/"):
            cls.api_url += "/"
        cls.api_url += "api"
    
    def test_get_unauthorized(self):
        """Test that GET requests without authorization are rejected."""
        # ACT
        response = requests.get(self.api_url)
        
        # ASSERT
        assert response.status_code == 401
        assert "Unauthorized" in response.text
    
    def test_get_authorized(self):
        """Test that GET requests with valid authorization are accepted."""
        # ARRANGE
        headers = {
            "Authorization": "Bearer allow-me-access"
        }
        
        # ACT
        response = requests.get(self.api_url, headers=headers)
        
        # ASSERT
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert data["message"] == "This is a mock response for GET"
    
    def test_post_authorized(self):
        """Test that POST requests with valid authorization are accepted."""
        # ARRANGE
        headers = {
            "Authorization": "Bearer allow",
            "Content-Type": "application/json"
        }
        payload = {
            "test": "data"
        }
        
        # ACT
        response = requests.post(self.api_url, headers=headers, json=payload)
        
        # ASSERT
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert data["message"] == "This is a mock response for POST"