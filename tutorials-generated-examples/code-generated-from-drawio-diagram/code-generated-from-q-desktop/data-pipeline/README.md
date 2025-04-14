# AWS CDK Step Functions Demo

This project implements a serverless workflow using AWS CDK v2 with Python. The architecture includes:

- A versioned S3 bucket with KMS encryption
- EventBridge integration to trigger on S3 events
- Step Functions workflow with 3 Lambda functions performing simple additions

## Project Structure

```
.
├── cdk/                    # CDK infrastructure code
│   ├── app.py             # CDK app entry point
│   ├── requirements.txt    # CDK Python dependencies
│   └── stacks/            # CDK stack definitions
│       └── main_stack.py  # Main infrastructure stack
├── lambda/                # Lambda function code
│   ├── lambda1/          # First Lambda (1+1)
│   ├── lambda2/          # Second Lambda (2+2)
│   └── lambda3/          # Third Lambda (3+3)
└── tests/                 # Unit tests
    ├── test_lambdas.py   # Lambda function tests
    └── test_stack.py     # CDK stack tests
```

## Setup Instructions

1. Install dependencies:
```bash
cd cdk
python -m pip install -r requirements.txt
```

2. Deploy the stack:
```bash
cd cdk
cdk deploy
```

3. Run tests:
```bash
python -m pytest tests/
```

## Architecture Overview

1. When a file is uploaded to the S3 bucket:
   - The bucket is versioned and encrypted with a KMS customer managed key
   - An EventBridge rule detects the S3 event

2. The EventBridge rule triggers a Step Functions workflow:
   - First Lambda performs 1+1 addition
   - Then two parallel Lambdas perform 2+2 and 3+3 additions

## Clean Up

To remove all resources:
```bash
cd cdk
cdk destroy
```