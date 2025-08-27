# Tutorial Index
1. [Generate Mermaid Flow Diagram from Code](#1-generate-mermaid-flow-diagram-from-code)
2. [Generate Mermaid Sequence Diagram from Code](#2-generate-mermaid-sequence-diagram-from-code)
3. [Generate Mermaid Class Diagram from Code](#3-generate-mermaid-class-diagram-from-code)
4. [Generate Code from Mermaid Diagram](#4-generate-code-from-mermaid-diagram)
5. [Generate Code from Drawio Diagram](#5-generate-code-from-drawio-diagram)
6. [Generate Drawio Flow Diagram from Code](#6-generate-drawio-flow-diagram-from-code)
7. [Split Drawio Diagram into CDK Constructs](#7-split-drawio-diagram-into-cdk-constructs)

## 1. Generate Mermaid Flow Diagram from Code

### Script to execute In VS Code terminal (```~/wio-from-diagram-to-code-with-amazon-q-developer/_playground/vscode-app-folder$```)
```
../init-playground.sh --with-starting-point-folder=feedback-app-code
```

### Prompts to execute In Q Desktop, Q CLI, Kiro, ...
```
create a mermaid flow diagram of my application (data flow from up to bottom, use colors, keep formatting simple)
```

### Result Example
![mermaid architecture diagram from code](../screenshots/mermaid-architecture-diagram-from-code.png)

## 2. Generate Mermaid Sequence Diagram from Code

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

## 3. Generate Mermaid Class Diagram from Code

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

## 4. Generate Code from Mermaid Diagram

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

## 5. Generate Code from Drawio Diagram

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

## 6. Generate Drawio Flow Diagram from Code

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

