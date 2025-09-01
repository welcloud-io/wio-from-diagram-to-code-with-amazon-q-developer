import sys
import os
import json
import pytest
from unittest import mock

# Add the lambda directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lambda')))

# Import the handler function from the authorizer module
from authorizer import handler, generate_policy

def test_generate_policy():
    """Test the generate_policy function."""
    # ARRANGE
    principal_id = "test-user"
    effect = "Allow"
    resource = "arn:aws:execute-api:us-east-1:123456789012:api-id/stage/method/resource"
    
    # ACT
    policy = generate_policy(principal_id, effect, resource)
    
    # ASSERT
    assert policy["principalId"] == principal_id
    assert policy["policyDocument"]["Version"] == "2012-10-17"
    assert len(policy["policyDocument"]["Statement"]) == 1
    assert policy["policyDocument"]["Statement"][0]["Effect"] == effect
    assert policy["policyDocument"]["Statement"][0]["Resource"] == resource
    assert policy["policyDocument"]["Statement"][0]["Action"] == "execute-api:Invoke"
    assert "context" in policy

def test_authorizer_allow():
    """Test the authorizer handler with a valid token."""
    # ARRANGE
    event = {
        "type": "TOKEN",
        "authorizationToken": "Bearer allow-me-access",
        "methodArn": "arn:aws:execute-api:us-east-1:123456789012:api-id/stage/method/resource"
    }
    context = {}
    
    # ACT
    with mock.patch('authorizer.print') as mock_print:
        result = handler(event, context)
    
    # ASSERT
    assert result["principalId"] == "user"
    assert result["policyDocument"]["Statement"][0]["Effect"] == "Allow"
    assert result["policyDocument"]["Statement"][0]["Resource"] == event["methodArn"]
    mock_print.assert_called_once()

def test_authorizer_deny():
    """Test the authorizer handler with an invalid token."""
    # ARRANGE
    event = {
        "type": "TOKEN",
        "authorizationToken": "Bearer invalid-token",
        "methodArn": "arn:aws:execute-api:us-east-1:123456789012:api-id/stage/method/resource"
    }
    context = {}
    
    # ACT
    with mock.patch('authorizer.print') as mock_print:
        result = handler(event, context)
    
    # ASSERT
    assert result["principalId"] == "user"
    assert result["policyDocument"]["Statement"][0]["Effect"] == "Deny"
    assert result["policyDocument"]["Statement"][0]["Resource"] == event["methodArn"]
    mock_print.assert_called_once()

def test_authorizer_exception():
    """Test the authorizer handler when an exception occurs."""
    # ARRANGE
    event = {
        "type": "TOKEN",
        # Missing authorizationToken to trigger an exception
        "methodArn": "arn:aws:execute-api:us-east-1:123456789012:api-id/stage/method/resource"
    }
    context = {}
    
    # ACT
    with mock.patch('authorizer.print') as mock_print:
        result = handler(event, context)
    
    # ASSERT
    assert result["principalId"] == "user"
    assert result["policyDocument"]["Statement"][0]["Effect"] == "Deny"
    assert result["policyDocument"]["Statement"][0]["Resource"] == event["methodArn"]
    # The handler only logs the event, not the error in our implementation
    assert mock_print.call_count >= 1