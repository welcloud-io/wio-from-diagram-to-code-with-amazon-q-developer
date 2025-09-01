# File Processing Application

This application creates an AWS infrastructure for processing files uploaded to an S3 bucket using a Lambda function, which then sends the processed data to a third-party API.

## Architecture

The application consists of:
- An S3 bucket that receives file uploads
- A Lambda function triggered by S3 object creation events
- Integration with a third-party API for file processing

## Development

### Prerequisites

- Python 3.9 or higher
- AWS CDK v2
- AWS CLI configured with appropriate credentials

### Setup

1. Install dependencies:
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

2. Deploy the stack:
```
cdk deploy
```

## Testing

### Running Tests

To run all tests:
```
pytest
```

To run tests with coverage:
```
pytest --cov=cdk_app --cov=lambda
```

### Test Structure

- `tests/unit/cdk_app/`: Tests for CDK infrastructure
- `tests/unit/lambda/`: Tests for Lambda function logic

## Cleanup

To destroy the deployed resources:
```
cdk destroy
```
