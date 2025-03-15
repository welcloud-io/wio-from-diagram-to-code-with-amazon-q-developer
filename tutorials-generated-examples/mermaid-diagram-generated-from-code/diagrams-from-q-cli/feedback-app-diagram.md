# Feedback Application Architecture

```mermaid
graph TD
    User[User] -->|Access| API[API Gateway]
    
    subgraph "AWS Cloud"
        API -->|GET /| LandingPage[Landing Page Function]
        API -->|POST /feedbacks| FeedbackFunc[Record & Confirm Feedback Function]
        
        LandingPage -->|Returns| HTML[HTML Form]
        HTML -->|Submit Feedback| API
        
        FeedbackFunc -->|Store Data| DynamoDB[(DynamoDB Table)]
        FeedbackFunc -->|Send Notification| SNS{SNS Topic}
        
        SNS -->|SMS| UserPhone[User Phone]
    end
    
    classDef aws fill:#FF9900,stroke:#232F3E,color:white;
    classDef lambda fill:#009900,stroke:#232F3E,color:white;
    classDef frontend fill:#3366CC,stroke:#232F3E,color:white;
    
    class API,DynamoDB,SNS aws;
    class LandingPage,FeedbackFunc lambda;
    class HTML,User,UserEmail frontend;
```

## Application Flow

1. User accesses the application through API Gateway
2. Landing Page Function serves the HTML form
3. User submits feedback via the form
4. API Gateway routes the POST request to the Record & Confirm Feedback Function
5. The function stores the feedback in DynamoDB
6. The function sends a confirmation notification via SNS
7. User receives a confirmation email

## Components

- **API Gateway**: Handles HTTP requests
- **Landing Page Function**: Lambda function that serves the HTML form
- **Record & Confirm Feedback Function**: Lambda function that processes feedback submissions
- **DynamoDB Table**: Stores feedback data
- **SNS Topic**: Sends email notifications