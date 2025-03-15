# 0 - Start tutorials (More) playground ( i.e. new VS Code Window)

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

# 1 - S3 Notification

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$ ../init-playground-more.sh 
Available tutorials:
1. S3 notification (from diagram to code)
2. Data pipeline (from diagram to code)
3. Deployment pipeline (from diagram to code)
Which tutorial would you like to view? (1-3): 1
```

## 1.1 - Generate lambda code only

| **@workspace generate lambda function code in python from diagram**

## 1.2 - Generate infrastructure only

| **@workspace generate python cdk V2 template from diagram**

# 2 - Data pipeline

### Initialize tutorial

```bash
# From VS Code tutorial window terminal
$ ../init-playground-more.sh 
Available tutorials:
1. S3 notification (from diagram to code)
2. Data pipeline (from diagram to code)
3. Deployment pipeline (from diagram to code)
Which tutorial would you like to view? (1-3): 2
```

| @workspace generate infrastructure with CDK V2 (be aware that you have a step functions workflow with lambda orchestration in the diagram)

# 3 - Deployment Pipeline

```bash
# From VS Code tutorial window terminal
$ ../init-playground-more.sh 
Available tutorials:
1. S3 notification (from diagram to code)
2. Data pipeline (from diagram to code)
3. Deployment pipeline (from diagram to code)
Which tutorial would you like to view? (1-3): 3
```

| @workspace can you generate the deployment pipeline with python cdk v2 from my diagram

