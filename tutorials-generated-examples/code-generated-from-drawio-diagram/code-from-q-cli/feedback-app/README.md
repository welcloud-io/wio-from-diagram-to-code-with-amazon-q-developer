# Feedback Application

This is a serverless feedback application built with AWS services and CDK v2. The application allows users to submit feedback through a web form, stores the feedback in a DynamoDB table, and sends confirmation emails via SNS.

## Architecture

The application consists of the following components:

- **API Gateway**: Provides HTTP endpoints for the landing page and feedback submission
- **Lambda Functions**:
  - Landing Page Function: Serves the HTML form for feedback submission
  - Record and Confirm Feedback Function: Processes feedback submissions, stores data in DynamoDB, and sends notifications
- **DynamoDB Table**: Stores feedback data
- **SNS Topic**: Sends confirmation emails

## Prerequisites

- AWS CLI configured with appropriate credentials
- Python 3.9 or later
- Node.js 14 or later
- AWS CDK v2 installed

## Deployment Instructions

1. Install the required dependencies:

```bash
cd cdk_app
pip install -r requirements.txt
npm install -g aws-cdk
```

2. Update the email address in `cdk_app/app.py` to receive feedback notifications.

3. Deploy the application:

```bash
cdk bootstrap  # Only needed for first-time CDK users
cdk deploy
```

4. After deployment, the CDK will output the API Gateway URL. Use this URL to access the feedback form.

## Usage

1. Open the landing page URL in a web browser
2. Fill out the feedback form with your name, email, feedback text, and rating
3. Submit the form
4. You will receive a confirmation message on the page
5. A confirmation email will be sent to the configured email address

## Cleanup

To remove all resources created by this application:

```bash
cdk destroy
```

## Customization

- To modify the feedback form, edit the HTML in `lambda_functions/landing_page.py`
- To change the feedback processing logic, edit `lambda_functions/record_feedback.py`
- To adjust the infrastructure configuration, modify `cdk_app/app.py`