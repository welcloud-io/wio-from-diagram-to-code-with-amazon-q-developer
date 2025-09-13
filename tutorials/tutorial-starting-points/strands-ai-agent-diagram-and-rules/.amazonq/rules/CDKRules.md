When asked to generate a CDK project
- Create a dedicated folder for each lamda
- Name lambda function explictly
- Destroy of any resource (like dynamodb tables, S3 buckets, ...) when CDK Stack is destoyed
- Give necessary permissions to the lambda to call aws services
- Be consistent, use the api gateway stage names in html pages