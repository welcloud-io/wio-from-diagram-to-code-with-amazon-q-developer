# 0 - Start tutorials (More) playground ( i.e. new VS Code Window)

The command below will open a new VS Code window. 
That means you will have a blank playground where you will import a tutorial starting point.

```bash
# From wio-from-diagram-to-code-with-amazon-q-developer/
$> ./start-vscode-tutorial-window.sh
```

If something doesn't work in this tutorial, these commands can help:

Remove amazonq cache content  
 ```$> rm ~/.aws/amazonq/cache/cache/*```
 
 Reload VS Code window  
 ```Ctrl / Shift / P / Developer: Reload Window```

 OR
 
 ``` ../init-playground.sh --hard ```

which removes all files in the playground folder and amazonq cache content (that does not reload window)

# 1 - S3 Notification

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$ ../init-playground.sh 

Available starting points:

0. Empty Folder (from Code to Diagram)
1. Feedback App Code (from Code to Diagram)
2. Feedback App Diagram (from Diagram to Code)
3. S3 notification (from Diagram to Code)
4. Data pipeline (from Diagram to Code)
5. Deployment pipeline (from Diagram to Code)

Where do you want to start from (0-5)?: 3
```

## 1.1 - Generate lambda code only

| **@workspace generate lambda function code in python from diagram**

## 1.2 - Generate infrastructure only

| **@workspace generate python cdk V2 template from diagram**

# 2 - Data pipeline

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$ ../init-playground.sh 

Available starting points:

0. Empty Folder (from Code to Diagram)
1. Feedback App Code (from Code to Diagram)
2. Feedback App Diagram (from Diagram to Code)
3. S3 notification (from Diagram to Code)
4. Data pipeline (from Diagram to Code)
5. Deployment pipeline (from Diagram to Code)

Where do you want to start from (0-5)?: 4
```

| @workspace generate infrastructure with CDK V2 (be aware that you have a step functions workflow with lambda orchestration in the diagram)

# 3 - Deployment Pipeline

```bash
# From VS Code tutorial window terminal
$ ../init-playground.sh 

Available starting points:

0. Empty Folder (from Code to Diagram)
1. Feedback App Code (from Code to Diagram)
2. Feedback App Diagram (from Diagram to Code)
3. S3 notification (from Diagram to Code)
4. Data pipeline (from Diagram to Code)
5. Deployment pipeline (from Diagram to Code)

Where do you want to start from (0-5)?: 5
```

| @workspace can you generate the deployment pipeline with python cdk v2 from my diagram

