# Feedback App Project Original Generated Diagram

prompt: @workspace can you generate a mermaid diagram of my application

```mermaid	
graph TD
    A[User] -->|HTTP GET /| B[API Gateway]
    B -->|Invoke| C[Landing Page Function]
    C -->|Return HTML| B
    B -->|Return HTML| A

    A -->|HTTP POST /feedbacks| B
    B -->|Invoke| D[Send Feedback Function]
    D -->|Write| E[(DynamoDB Table)]
    D -->|Publish| F[SNS Topic]
    F -->|Send Email| G[User Email]

    subgraph AWS Cloud
        B
        C
        D
        E
        F
    end
```


## Sequence Diagram

prompt:@workspace can you generate a mermaid sequence diagram of the application

```mermaid
sequenceDiagram
    participant User
    participant API Gateway
    participant LandingPageFunction
    participant RecordAndConfirmFunction
    participant DynamoDB
    participant SNS
    participant AdminEmail

    User->>API Gateway: GET /
    API Gateway->>LandingPageFunction: Invoke
    LandingPageFunction->>API Gateway: Return HTML landing page
    API Gateway->>User: Display landing page

    User->>API Gateway: POST /feedbacks
    API Gateway->>RecordAndConfirmFunction: Invoke
    RecordAndConfirmFunction->>DynamoDB: Store feedback
    DynamoDB-->>RecordAndConfirmFunction: Confirm storage
    RecordAndConfirmFunction->>SNS: Publish feedback notification
    SNS-->>RecordAndConfirmFunction: Confirm publication
    SNS->>AdminEmail: Send email notification
    RecordAndConfirmFunction->>API Gateway: Return confirmation
    API Gateway->>User: Display confirmation
```

## Class Diagram

@workspace can you generate a mermaid class diagram of the application

```mermaid
classDiagram
    class User {
        +submitFeedback()
        +viewLandingPage()
    }

    class APIGateway {
        +routeRequest()
    }

    class LandingPageFunction {
        -HTML_TEMPLATE: string
        +handleRequest()
        -generateHTML()
    }

    class RecordAndConfirmFunction {
        +handleRequest()
        -storeFeedback()
        -publishNotification()
        -generateConfirmation()
    }

    class Feedback {
        +id: string
        +content: string
        +timestamp: datetime
        +userId: string
    }

    class DynamoDB {
        +putItem()
        +getItem()
    }

    class SNSTopic {
        +publish()
    }

    class AdminNotification {
        +recipientEmail: string
        +subject: string
        +body: string
    }

    User --> APIGateway: interacts with
    APIGateway --> LandingPageFunction: routes to
    APIGateway --> RecordAndConfirmFunction: routes to
    RecordAndConfirmFunction --> Feedback: creates
    RecordAndConfirmFunction --> DynamoDB: uses
    RecordAndConfirmFunction --> SNSTopic: publishes to
    SNSTopic --> AdminNotification: sends
    DynamoDB --> Feedback: stores
```