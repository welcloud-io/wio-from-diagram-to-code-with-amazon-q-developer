# Serverless Web Application

This project implements a serverless web application based on the hand-drawn architecture diagram. The application uses AWS Lambda for compute, API Gateway for HTTP routing, and AWS CDK v2 for infrastructure as code.

## Architecture

```
User → Desktop/Browser → Amazon API Gateway → AWS Lambda (Landing Page)
```

## Components

- **Frontend**: HTML/CSS/JavaScript served directly from Lambda
- **API Gateway**: Amazon API Gateway handles HTTP requests and routing
- **Backend**: AWS Lambda function written in Python 3.11
- **Infrastructure**: AWS CDK v2 (Python) for Infrastructure as Code

## Project Structure

```
├── app.py                          # CDK app entry point
├── cdk.json                        # CDK configuration
├── requirements.txt                # Python dependencies
├── serverless_web_app/
│   ├── __init__.py
│   └── serverless_web_app_stack.py # CDK stack definition
├── lambda/
│   └── landing_page.py             # Lambda function code
└── README.md                       # This file
```

## Prerequisites

- Python 3.8 or later
- Node.js 14.x or later
- AWS CLI configured with appropriate credentials
- AWS CDK CLI installed (`npm install -g aws-cdk`)

## Setup and Deployment

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Bootstrap CDK (first time only):**
   ```bash
   cdk bootstrap
   ```

3. **Deploy the stack:**
   ```bash
   cdk deploy
   ```

4. **View the application:**
   After deployment, the CDK will output the API Gateway URL. Open this URL in your browser to see the landing page.

## Development

### Local Testing

You can test the Lambda function locally:

```python
# Test the Lambda function
from lambda.landing_page import handler

# Mock event
event = {
    'httpMethod': 'GET',
    'path': '/',
    'headers': {},
    'queryStringParameters': None
}

# Test the handler
response = handler(event, None)
print(response)
```

### CDK Commands

- `cdk ls` - List all stacks
- `cdk synth` - Synthesize CloudFormation template
- `cdk deploy` - Deploy the stack
- `cdk diff` - Compare deployed stack with current state
- `cdk destroy` - Delete the stack

## Features

- **Serverless Architecture**: No servers to manage, pay only for what you use
- **Auto-scaling**: Automatically scales based on demand
- **CORS Enabled**: Cross-Origin Resource Sharing configured
- **Error Handling**: Comprehensive error handling and logging
- **Responsive Design**: Mobile-friendly landing page
- **Infrastructure as Code**: Entire infrastructure defined in code

## Monitoring and Logs

- Lambda function logs are available in CloudWatch Logs
- API Gateway access logs and execution logs can be enabled
- CloudWatch metrics are automatically collected

## Security Features

- API Gateway throttling configured (100 requests/second, 200 burst)
- Lambda function runs with minimal IAM permissions
- CORS properly configured for web browser access

## Cost Optimization

- Lambda function configured with 128MB memory (minimum)
- CloudWatch log retention set to 1 week
- API Gateway caching can be enabled for better performance

## Customization

### Modifying the Landing Page

Edit `lambda/landing_page.py` and update the `generate_landing_page_html()` function to customize the HTML content.

### Adding New Endpoints

1. Create new Lambda functions in the `lambda/` directory
2. Add them to the CDK stack in `serverless_web_app_stack.py`
3. Create new API Gateway resources and methods

### Environment Variables

Add environment variables to Lambda functions in the CDK stack:

```python
landing_page_lambda = _lambda.Function(
    # ... other parameters
    environment={
        'ENVIRONMENT': 'production',
        'LOG_LEVEL': 'INFO'
    }
)
```

## Troubleshooting

### Common Issues

1. **CDK Bootstrap Error**: Run `cdk bootstrap` in your target AWS region
2. **Permission Denied**: Ensure your AWS credentials have sufficient permissions
3. **Lambda Timeout**: Increase timeout in the CDK stack if needed
4. **API Gateway 502 Error**: Check Lambda function logs in CloudWatch

### Useful Commands

```bash
# View CloudFormation events
aws cloudformation describe-stack-events --stack-name ServerlessWebAppStack

# View Lambda logs
aws logs describe-log-groups --log-group-name-prefix /aws/lambda/ServerlessWebAppStack

# Test API Gateway endpoint
curl -X GET https://your-api-id.execute-api.region.amazonaws.com/prod/
```

## Next Steps

- Add authentication with Amazon Cognito
- Implement a database with DynamoDB
- Add CI/CD pipeline with AWS CodePipeline
- Implement monitoring and alerting
- Add custom domain name with Route 53
- Implement caching with CloudFront

## License

This project is licensed under the MIT License.
