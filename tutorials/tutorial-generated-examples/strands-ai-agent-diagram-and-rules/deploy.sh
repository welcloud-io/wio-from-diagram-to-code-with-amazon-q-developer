#!/bin/bash

# Install Strands packages in layer
cd layers/strands
pip install -r requirements.txt -t python/
cd ../..

# Deploy CDK stack
cdk bootstrap
cdk deploy --require-approval never