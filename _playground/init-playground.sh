#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

echo
echo "Available starting points:"
echo
echo "0. Empty Folder (from Code to Diagram)"
echo "1. Feedback App Code (from Code to Diagram)"
echo "2. Feedback App Diagram (from Diagram to Code)"
echo "3. S3 notification (from Diagram to Code)"
echo "4. Data pipeline (from Diagram to Code)"
echo "5. Deployment pipeline (from Diagram to Code)"
echo

# Prompt user to select tutorial
read -p "Where do you want to start from (0-5)?: " tutorial_choice

# Validate input
if [[ ! $tutorial_choice =~ ^[0-5]$ ]]; then
    echo "Invalid selection. Please choose a number between 0 and 5."
    exit 1
fi

if [ $tutorial_choice != '5' ]; then
   ../clear-playground.sh $1
fi

# -----------------------------------------------------------------------------
# Starting points preparation
# -----------------------------------------------------------------------------

prepare_playground_feedback_app_code() {

cp -r ../../tutorials-starting-points/feedback-app-code/* .

cat << 'EOF' > MERMAID-DIAGRAMS.md
```mermaid
<PUT MERMAID CODE HERE AND CLICK ON PREVIEW AT THE RIGHT HAND CORNER>
```
EOF

cat << 'EOF' > APP.DRAWIO.XML
<PUT GENERATED DIAGRAM HERE>
EOF

}

prepare_playground_empty_folder() {

echo
   
}

prepare_playground_feedback_app_diagram() {

cp -r ../../tutorials-starting-points/feedback-app-diagram/* .
   
}

prepare_playground_s3_notification() {

cp -r ../../tutorials-starting-points/s3-notification-diagram/* .
   
}

prepare_playground_data_pipeline() {

cp -r ../../tutorials-starting-points/data-pipeline-diagram/* .
   
}

prepare_playground_deployment_pipeline() {

cp -r ../../tutorials-starting-points/deployment-pipeline/* .
   
}

# -----------------------------------------------------------------------------
# Tutorials descriptions
# -----------------------------------------------------------------------------
tutorial_description_0() {
echo """
0. Empty Folder...

$(tput bold)$(tput setaf 2)TUTORIAL [From Mermaid Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

-> Go to Q Desktop and enter

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
1. Feedback App Code (from code to diagram)...

$(tput bold)$(tput setaf 2)TUTORIAL [From Code to Mermaid Diagram with Q Desktop] PROMPTS:$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)N.B.: When using @workspace, 
      you might need to type @workspace in Q manually and then copy/paste the rest of the prompt$(tput sgr0)

-> Go to Q Desktop and type

$(tput bold)> @workspace can you generate a mermaid diagram of my application$(tput sgr0)

-> Copy/Paste prompt results in MERMAID-DIAGRAMS.md

$(tput bold)> @workspace can you generate a mermaid sequence diagram of the application$(tput sgr0)

-> Copy/Paste prompt results in MERMAID-DIAGRAMS.md

$(tput bold)> @workspace can you generate a mermaid class diagram of the application$(tput sgr0)

-> Copy/Paste prompt results in MERMAID-DIAGRAMS.md

$(tput bold)$(tput setaf 2)TUTORIAL [From Code to Drawio Diagram with Q Desktop] PROMPTS:$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)N.B.: When using @workspace, 
      you might need to type @workspace in Q manually and then copy/paste the rest of the prompt$(tput sgr0)

-> Go to Q Desktop and enter

$(tput bold)> @workspace generate a draw.io diagram in an xml format for this application (I want to use AWS 2024 Icons, lines should be orthogonal, dataflow from up to bottom)$(tput sgr0) 

-> Copy/Paste prompt results in APP.DRAWIO.XML (Open it with text editor)

-------------------------------------------------------------------------------
"""
}

tutorial_description_2() {
echo """
2. Feedback App Diagram (from Diagram to Code)...

$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

-> Open drawio diagram in folder.

-> Go to Q Desktop and enter:

$(tput bold)> /dev can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)$(tput sgr0)

-> Deploy generated code in your folder with 'cdk deploy'

$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q CLI]$(tput sgr0)
-------------------------------------------------------------------------------

-> Open terminal and type:

$> q chat

$(tput bold)> can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)$(tput sgr0)

-> Say yes (y) to all

$(tput bold)> modify the drawio diagram to split the architecture diagram into well defined cdk construts (use colors and legend)$(tput sgr0)

-> Say yes (y) to all

-> Deploy generated code in your folder with 'cdk deploy'

-------------------------------------------------------------------------------
"""
}

tutorial_description_3() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

$(tput bold)N.B.: When using @workspace, 
      you might need to type @workspace in Q manually and then copy/paste the rest of the prompt$(tput sgr0)

-> To generate lambda code only, type:

$(tput bold)> @workspace generate lambda function code in python from diagram$(tput sgr0)

-> To generate infrastructure only, type:

$(tput bold)> @workspace generate python cdk V2 template from diagram$(tput sgr0)
"""
}

tutorial_description_4() {
echo """
$(tput bold)$(tput setaf 2)TUTORIAL [From Drawio Diagram to Code with Q Desktop]$(tput sgr0)
-------------------------------------------------------------------------------

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

if [ $tutorial_choice == '0' ]; then
prepare_playground_empty_folder
tutorial_description_0
fi

if [ $tutorial_choice == '1' ]; then
prepare_playground_feedback_app_code
tutorial_description_1
fi

if [ $tutorial_choice == '2' ]; then
prepare_playground_feedback_app_diagram
tutorial_description_2
fi

if [ $tutorial_choice == '3' ]; then
prepare_playground_s3_notification
tutorial_description_3
fi

if [ $tutorial_choice == '4' ]; then
prepare_playground_data_pipeline
tutorial_description_4
fi

if [ $tutorial_choice == '5' ]; then
prepare_playground_deployment_pipeline
tutorial_description_5
fi

