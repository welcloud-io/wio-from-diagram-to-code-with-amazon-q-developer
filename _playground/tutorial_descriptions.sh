# -----------------------------------------------------------------------------
# Tutorials descriptions
# -----------------------------------------------------------------------------
tutorial_description_0() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Mermaid Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)
> /dev can you generate application files from this mermaid diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)
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
$(tput sgr0)

-> Deploy generated code in your folder with 'cdk deploy'
-------------------------------------------------------------------------------
"""
}

tutorial_description_1() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Code to Mermaid Diagram with Q Desktop] PROMPTS:$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)> @workspace can you generate a mermaid diagram of my application$(tput sgr0)
$(tput bold)> @workspace can you generate a mermaid sequence diagram of the application$(tput sgr0)
$(tput bold)> @workspace can you generate a mermaid class diagram of the application$(tput sgr0)

$(tput bold)$(tput setaf 2)TUTORIAL [From Code to Drawio Diagram with Q Desktop] PROMPTS:$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)> @workspace generate a draw.io diagram in an xml format for this application (I want to use AWS 2024 Icons, lines should be orthogonal, dataflow from up to bottom)$(tput sgr0) 
-> Copy/Paste prompt results in APP.DRAWIO.XML (Open it with text editor)

-------------------------------------------------------------------------------
"""
}

tutorial_description_2() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)> /dev can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)$(tput sgr0)

$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q CLI]$(tput sgr0)
-------------------------------------------------------------------------------

$> q chat

$(tput bold)> can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)$(tput sgr0)
$(tput bold)> modify the drawio diagram to split the architecture diagram into well defined cdk construts (use colors and legend)$(tput sgr0)

-------------------------------------------------------------------------------
"""
}

tutorial_description_3() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)> @workspace generate lambda function code in python from diagram$(tput sgr0)
$(tput bold)> @workspace generate python cdk V2 template from diagram$(tput sgr0)
"""
}

tutorial_description_4() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)> @workspace generate lambda code in the drawio diagram (take notes into account)$(tput sgr0)
$(tput bold)> @workspace generate infrastructure with CDK V2 (be aware that you have a step functions workflow with lambda orchestration in the diagram)$(tput sgr0)
"""
}

tutorial_description_5() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)> @workspace can you generate the deployment pipeline with python cdk v2 from my diagram$(tput sgr0)
"""
}

tutorial_description_6() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q CLI]$(tput sgr0)
-------------------------------------------------------------------------------
"""
}

tutorial_description_7() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Hand Drawing to Code with Q CLI]$(tput sgr0)
-------------------------------------------------------------------------------

$> q chat --model claude-4-sonnet

> create a mermaid diagram from the hand-drawn-architecture.jpg file in this folder
> create a draw.io diagram from the hand-drawn-architecture.jpg (I want to use AWS 2024 Icons)
> can you generate application from the hand-drawn-architecture file (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)

"""
}

tutorial_description_8() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Hand Drawing to Code with Q CLI]$(tput sgr0)
-------------------------------------------------------------------------------

$> q chat --model claude-4-sonnet

> create a mermaid diagram from the hand-drawn-architecture.jpg file in this folder. Keep all components at the original position. Note that ECR is outside the VPC.
> create a drawio diagram from the hand-drawn-architecture.jpg file in this folder. Keep all components at the original position.
> can you generate application from the hand-drawn-architecture.jpg file (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2).
> can you generate application from the hand-drawn-architecture.jpg file (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2). Keep it simple, don't add more than necessary, stick to the diagram intent.
"""
}

tutorial_description_9() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Hand Drawing to Code with Q CLI]$(tput sgr0)
-------------------------------------------------------------------------------

$> q chat --model claude-4-sonnet

> Create a mermaid diagram from hand-drawn-architecture.jpg file. Stick to the image, do not add more information.

"""
}

tutorial_description_10() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Hand Drawing to Code with Q CLI]$(tput sgr0)
-------------------------------------------------------------------------------

$> q chat --model claude-4-sonnet

> Create an application from the hand-drawn-graphical-interface.jpg file. I want a CDK serverless backend.
> create a drawio diagram of this application using AWS icons 2024 (dataflow from up to bottom)
> in the drawio diagram add a user desktop and separate cloufront/s3 data flow from api/lambda/dynamo data flow

"""
}
