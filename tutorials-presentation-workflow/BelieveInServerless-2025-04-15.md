### INIT

```../init-playground.sh --hard``` / 1 / (Ctrl-Shift P)

### General Questions

```What is S3 ?```

### @Workspace

```@workspace what does this application do?```

### Generate Diagram from Code

### From Code To Mermaid

```@workspace can you generate a mermaid sequence diagram of the application```

/home/olivier/wio-from-diagram-to-code-with-amazon-q-developer/tutorials-generated-examples/mermaid-diagram-generated-from-code/diagrams-from-q-desktop/feedback-app-generated-diagrams.md

### From Code To Drawio

```@workspace generate a draw.io diagram in an xml format for this application (I want to use AWS 2024 Icons, lines should be orthogonal, dataflow from up to bottom)```

/home/olivier/wio-from-diagram-to-code-with-amazon-q-developer/tutorials-generated-examples/drawio-diagram-generated-from-code/APP.DRAWIO.XML

```@APP.DRAWIO.XML is this well architected?```

### S3 notification

```../init-playground.sh --hard``` / 3 / (Ctrl-Shift P)

@diagram.drawio.xml can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)

### Data Pipeline with @workspace
```../init-playground.sh``` / 4

@diagram.drawio.xml generate python CDK V2 code and the lambda functions of the step functions workflow only

### Data Pipeline with /dev

```../init-playground.sh``` / 4

```/dev can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)```

```../init-playground.sh --with-result``` / 4

```cdk deploy --app "python3 app.py"```

### Feedback app with /dev

```../init-playground.sh --with-result``` / 2


### Q CLI

```../init-playground.sh``` / 6

```bash
$> q chat can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)
```

STOP HERE

### IMPROVE DETERMINISM

```../init-playground.sh --with-q-rules``` / 6

```/context show```

```../init-playground.sh --hard --with-rules``` / 5 /  (Ctrl-Shift P)

```@diagram.drawio.xml generate workflow with lambda functions only```


### Deployment Pipeline

```../init-playground.sh / 5```

```@diagram.drawio.xml can you generate the deployment pipeline with python cdk v2 from my diagram```

