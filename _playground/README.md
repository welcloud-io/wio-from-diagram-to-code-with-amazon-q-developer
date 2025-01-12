!!! Each tutorial must be initialized in VSCode to work !!!

In the terminal type '../init-playground.sh' in the 'vscode-app-folder'

```bash
$.../vscode-app-folder> ../init-playground.sh
Available tutorials:
1. From code to diagram with Mermaid
2. From diagram to code with Mermaid
3. From diagram to code with draw.io
4. From code to diagram with draw.io
Which tutorial would you like to view? (1-4): ...
```

If something does not work, that can help:

 ```rm ~/.aws/amazonq/cache/cache/*```
 
 ```Ctrl / Shift / P / Developer: Reload Window```

# 1 - From Code to Diagram with Mermaid

### Initialize playgorund:

```bash
$.../vscode-app-folder> ../init-playground.sh
---choose corresponding tutorial---
```

## 1 - 1 - Generate Application diagram

Q prompt:

| **@workspace can you generate a mermaid diagram of my application**

Open .md file and add generated response

Click on preview, to preview .md file

## 1 - 2 - Generate Sequence diagram

Q prompt:

| **@workspace can you generate a mermaid sequence diagram of the application**

Open .md file and add generated response

Click on preview, to preview .md file

## 1 - 3 - Generate Class diagram

Q prompt:

| **@workspace can you generate a mermaid class diagram of the application**

Open .md file and add generated response

Click on preview, to preview .md file

# 2 - From Diagram to Code with Mermaid

### Initialize playgorund:

```bash
$.../vscode-app-folder> ../init-playground.sh
---choose corresponding tutorial---
```

Q Prompt

| **/dev can you generate application files from this mermaid diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)**

```
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

Deploy the application
```bash
cdk deploy --app "python3 app.py"
```

Fix the generated result using inline chat (Ctrl-I):


| **I want my feedback data to be sent as a json document to the '/prod/feebacks' endpoint with a field called "feedback" containing the feedback value typed into the html form**

# 3 - From Diagram to Code with Draw.io

### Initialize playgorund:

```bash
$.../vscode-app-folder> ../init-playground.sh
---choose corresponding tutorial---
```

You can open draw.io diagram in VSCode

Q Prompt:

| **/dev can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)**


# Generate drawio diagram from application

### Initialize playgorund:

```bash
$.../vscode-app-folder> ../init-playground.sh
---choose corresponding tutorial---
```

| **@workspace generate a draw.io diagram in an xml format for this application (I want to use AWS 2024 Icons, lines should be orthogonal, dataflow from up to bottom)**

In case of an error when opening the diagram, add this to your prompt, that can slve the issue:

| **I got an error when I want to open diagram**

