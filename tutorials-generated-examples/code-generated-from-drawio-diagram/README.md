# Feedback System

This is a serverless feedback system built with AWS CDK v2 that includes:
- A landing page with a feedback form
- API Gateway endpoints
- DynamoDB storage
- SNS notification system

## Prerequisites
- AWS CDK v2
- Python 3.9 or higher
- AWS CLI configured with appropriate credentials

## Setup
1. Create a virtual environment:
```
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Update the email subscription in `stacks/feedback_stack.py` with your email address.

4. Deploy the stack:
```
cdk deploy
```

## Usage
After deployment, you'll receive the API Gateway URL. Access this URL to see the feedback form.

## Clean Up
To remove all resources:
```
cdk destroy
```