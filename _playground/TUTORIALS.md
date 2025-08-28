# Tutorial Index
1. [Generate Mermaid Architecture Diagram from Code - Feedback App](#1-generate-mermaid-architecture-diagram-from-code---feedback-app)
2. [Generate Mermaid Sequence Diagram from Code - Feedback App](#2-generate-mermaid-sequence-diagram-from-code---feedback-app)
3. [Generate Mermaid Class Diagram from Code - Feedback App](#3-generate-mermaid-class-diagram-from-code---feedback-app)
4. [Generate Code from Mermaid Diagram - Feedback App](#4-generate-code-from-mermaid-diagram---feedback-app)
5. [Generate Code from Drawio Diagram - Feedback App](#5-generate-code-from-drawio-diagram---feedback-app)
6. [Generate Drawio Architecture Diagram from Code - Feedback App](#6-generate-drawio-architecture-diagram-from-code---feedback-app)
7. [Split Drawio Diagram into CDK Constructs](#7-split-drawio-diagram-into-cdk-constructs)
8. [Generate Code from Drawio Diagram - S3 Notification](#8-generate-code-from-drawio-diagram---s3-notification)
9. [Generate Code from Drawio Diagram - Step Functions](#9-generate-code-from-drawio-diagram---step-functions)
10. [Generate Code from Drawio Diagram - Deployment Pipeline](#10-generate-code-from-drawio-diagram---deployment-pipeline)
11. [Generate Code from Drawio Diagram - API Gateway](#11-generate-code-from-drawio-diagram---api-gateway)
12. [Generate Code from HandDrawn Diagram - Landing Page](#12-generate-code-from-handdrawn-diagram---landing-page)
13. [Generate Code from HandDrawn Diagram - ECS App](#13-generate-code-from-handdrawn-diagram---ecs-app)
14. [Generate Code from HandDrawn Diagram - GUI](#14-generate-code-from-handdrawn-diagram---gui)

## 1. Generate Mermaid Architecture Diagram from Code - Feedback App

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid architecture diagram of my application (data flow from up to bottom, use colors, keep formatting simple)
```

### Result Example
![mermaid architecture diagram from code](../screenshots/mermaid-architecture-diagram-from-code.png)

## 2. Generate Mermaid Sequence Diagram from Code - Feedback App

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid sequence diagram of the application
```

### Result Example
![mermaid sequence diagram from code](../screenshots/mermaid-sequence-diagram-from-code.png)

## 3. Generate Mermaid Class Diagram from Code - Feedback App

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid class diagram of the application
```

### Result Example
![mermaid class diagram from code](../screenshots/mermaid-class-diagram-from-code.png)

## 4. Generate Code from Mermaid Diagram - Feedback App

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=empty
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
can you generate application files from this mermaid diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)
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

### Result Example
![code from mermaid diagram](../screenshots/code-from-mermaid-diagram.png)

## 5. Generate Code from Drawio Diagram - Feedback App

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-diagram
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)
```

### Result Example
![code from drawio diagram](../screenshots/code-from-drawio-diagram.png)

## 6. Generate Drawio Architecture Diagram from Code - Feedback App

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a draw.io diagram in an xml format for this application (I want to use AWS 2024 Icons, lines should be orthogonal, dataflow from up to bottom)
```

### Result Example
![drawio architecture diagram from code](../screenshots/drawio-architecture-diagram-from-code.png)

## 7. Split Drawio Diagram into CDK Constructs

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-diagram
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
modify the drawio diagram to split the architecture diagram into well defined cdk construts (use colors and legend)
```

### Result Example
![drawio split diagram into cdk constructs](../screenshots/drawio-split-diagram-into-cdk-constructs.png)

## 8. Generate Code from Drawio Diagram - S3 Notification

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=s3-notification-diagram
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
generate lambda function code in python from diagram
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
generate python cdk V2 template from diagram
```

### Result Example
![code from drawio diagram s3 notification](../screenshots/code-from-drawio-diagram-s3-notification.png)

## 9. Generate Code from Drawio Diagram - Step Functions

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=data-pipeline-diagram
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
generate lambda code in the drawio diagram (take notes into account)
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
generate infrastructure with CDK V2 (be aware that you have a step functions workflow with lambda orchestration in the diagram)
```

### Result Example
![code from drawio diagram data pipeline](../screenshots/code-from-drawio-diagram-data-pipeline.png)

## 10. Generate Code from Drawio Diagram - Deployment Pipeline

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=deployment-pipeline
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
can you generate the deployment pipeline with python cdk v2 from my diagram
```

### Result Example
![code from drawio diagram deployment pipeline](../screenshots/code-from-drawio-diagram-deployment-pipeline.png)

## 11. Generate Code from Drawio Diagram - API Gateway

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=api-gateway-diagram --with-q-rules
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
generate application
```

### Result Example
![code from drawio diagram api gateway](../screenshots/code-from-drawio-diagram-api-gateway.png)

## 12. Generate Code from HandDrawn Diagram - Landing Page

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=lambda-app-hand-drawn-diagram
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid diagram from the hand-drawn-architecture.jpg file in this folder
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a draw.io diagram from the hand-drawn-architecture.jpg (I want to use AWS 2024 Icons)
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
can you generate application from the hand-drawn-architecture file (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)
```

### Result Example
![code from handdrawn diagram landing page](../screenshots/code-from-handdrawn-diagram-landing-page.png)

## 13. Generate Code from HandDrawn Diagram - ECS App

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=ecs-app-hand-drawn-diagram
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid diagram from the hand-drawn-architecture.jpg file in this folder. Keep all components at the original position. Note that ECR is outside the VPC.
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a drawio diagram from the hand-drawn-architecture.jpg file in this folder. Keep all components at the original position.
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
can you generate application from the hand-drawn-architecture.jpg file (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2).
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
can you generate application from the hand-drawn-architecture.jpg file (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2). Keep it simple, don't add more than necessary, stick to the diagram intent.
```

### Result Example
![code from handdrawn diagram ecs app](../screenshots/code-from-handdrawn-diagram-ecs-app.png)

## 14. Generate Code from HandDrawn Diagram - GUI

### Make sure you have installed the [prerequisites](../README.md#prerequisites)
### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-hand-drawn-diagram
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
Create an application from the hand-drawn-graphical-interface.jpg file. I want a CDK serverless backend.
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a drawio diagram of this application using AWS icons 2024 (dataflow from up to bottom)
```
### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
in the drawio diagram add a user desktop and separate cloufront/s3 data flow from api/lambda/dynamo data flow
```

### Result Example
![code from handdrawn diagram gui](../screenshots/code-from-handdrawn-diagram-gui.png)

