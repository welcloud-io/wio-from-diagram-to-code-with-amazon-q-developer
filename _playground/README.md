# 0 - Start tutorials playground ( i.e. new VS Code Window)

The next command will open a new VS Code window. So, you will have blank playground where you will execute the tutorials.

```bash
# From wio-from-diagram-to-code-with-amazon-q-developer/
$> ./start-vscode-tutorial-window.sh
```

If something does not work in a tutorial, these commands can help:

Remove amazonq cache content  
 ```$> rm ~/.aws/amazonq/cache/cache/*```
 
 Reload VS Code window  
 ```Ctrl / Shift / P / Developer: Reload Window```

 OR
 
 ``` ../init-playground.sh --hard ```

which removes all files in the playground folder and amazonq cache content (that does not reload window)

# 1 - From Code to Diagram with Mermaid

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$../init-playground.sh
Available tutorials:
1. From code to diagram with Mermaid
2. From diagram to code with Mermaid
3. From diagram to code with draw.io
4. From code to diagram with draw.io
Which tutorial would you like to view? (1-4): 1
```

## 1.1 - Generate Application diagram

Q prompt:

| **@workspace can you generate a mermaid diagram of my application**

Open the MERMAID-DIAGRAMS.md file in the folder and add the generated response.

Save the file and click on Preview on the right hand corner.

Click on preview, to preview .md file

## 1.2 - Generate Sequence diagram

Q prompt:

| **@workspace can you generate a mermaid sequence diagram of the application**

Open the MERMAID-DIAGRAMS.md file in the folder and add the generated response.

Save the file and click on Preview on the right hand corner.

Click on preview, to preview .md file

## 1.3 - Generate Class diagram

Q prompt:

| **@workspace can you generate a mermaid class diagram of the application**

Open the MERMAID-DIAGRAMS.md file in the folder and add the generated response.

Save the file and click on Preview on the right hand corner.

Click on preview, to preview .md file

# 2 - From Diagram to Code with Mermaid

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$../init-playground.sh
Available tutorials:
1. From code to diagram with Mermaid
2. From diagram to code with Mermaid
3. From diagram to code with draw.io
4. From code to diagram with draw.io
Which tutorial would you like to view? (1-4): 2
```

Q Prompt:


| **/dev can you generate application files from this mermaid diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)
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
end**

Accept changes, and try to deploy the application with the CK

#### CDK installation
```bash
$> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
$> . ~/.bashrc 
$> nvm install --lts
$> npm install -g aws-cdk
```

#### CDK packages installation
```bash
$> sudo apt install python3-pip # if pip not installed yet
$> pip install -r requirements.txt
```

#### Deploy the application (N.B. The AWS CLI must be configured with credentials)
```bash
cdk deploy --app "python3 app.py"
```

### Test & fix the generated result

# 3 - From Diagram to Code with Draw.io

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$../init-playground.sh
Available tutorials:
1. From code to diagram with Mermaid
2. From diagram to code with Mermaid
3. From diagram to code with draw.io
4. From code to diagram with draw.io
Which tutorial would you like to view? (1-4): 3
```

Q Prompt:

| **/dev can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)**

#### Deploy the application (N.B. The AWS CLI must be configured with credentials)
```bash
cdk deploy --app "python3 app.py"
```

# 4 - From Code to Diagram with Draw.io

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$../init-playground.sh
Available tutorials:
1. From code to diagram with Mermaid
2. From diagram to code with Mermaid
3. From diagram to code with draw.io
4. From code to diagram with draw.io
Which tutorial would you like to view? (1-4): 4
```

Q Prompt:

| **@workspace generate a draw.io diagram in an xml format for this application (I want to use AWS 2024 Icons, lines should be orthogonal, dataflow from up to bottom)**

### Update app.drawio.xml file & display the content

Select 'app.drawio.xml' file, right click, choose 'Open with...' and select 'Text Editor'

Copy & Paste generated XML document

Save the file, and double click on it to open it with the Drawio Integration extension

### Fix / Troubleshoot

In case of an error when opening the diagram, add this to your prompt, that can solve the issue:

| **I got an error when I want to open the diagram**