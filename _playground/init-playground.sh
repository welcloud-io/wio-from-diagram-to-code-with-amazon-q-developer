#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

if [[ "$@" =~ "--help" ]]; then
    echo "usage: $0 [--hard] [--no-clear] [--with-cdk-template] [--with-q-rules] [--with-result]"
    exit 0
fi

# -----------------------------------------------------------------------------
# Choose tutorial configurtaion 
# -----------------------------------------------------------------------------

if ! [[ "$@" =~ "--with-starting-point-folder=" ]]; then

    if ! [[ "$@" =~ "--hard" ]]; then
    echo
    echo -e "\033[33m-------------------------------------------------------------------------------\033[0m"
    echo -e "\033[33m# Refreshing the @workspace index can help when you don't get the expected result\033[0m"
    echo -e "\033[33m# If needed, use: '$0 --hard', then Ctrl+Shift+P => 'Developer: Reload Window'\033[0m"
    echo -e "\033[33m-------------------------------------------------------------------------------\033[0m"
    fi


    if [[ "$1" =~ ^[0-9]$|^10$ ]]; then
        tutorial_choice=$1
        shift
    else
        echo
        echo "Available starting points:"
        echo
        echo "0. Empty Folder (from Code to Diagram)"
        echo "1. Feedback App Code (from Code to Diagram)"
        echo "2. Feedback App Diagram (from Diagram to Code)"
        echo "3. S3 notification Diagram (from Diagram to Code)"
        echo "4. Data pipeline Diagram (from Diagram to Code)"
        echo "5. Deployment pipeline Diagram (from Diagram to Code)"
        echo "6. Api Gateway Diagram (from Diagram to Code)"
        echo "7. Simple Lambda App Hand Drawn Diagram (from HandDrawing to Code)"
        echo "8. Simple ECS App Hand Drawn Diagram (from HandDrawing to Code)"
        echo "9. Well Architected Pillar Hand Drawn Diagram (from HandDrawing to Code)"
        echo "10. Feedback App GUI Hand Drawn Diagram (from HandDrawing to Code)"
        echo

        # Prompt user to select tutorial
        read -p "Where do you want to start from ?: " tutorial_choice

        # Validate input
        if [[ ! $tutorial_choice =~ ^[0-9]$|^10$ ]]; then    
            echo "Invalid selection. Please choose a number between 0 and 10."
            exit 1
        fi
    fi
fi

# -----------------------------------------------------------------------------
# Clean files 
# --hard will delete cache & mcp.json file (but create a backup)
# -----------------------------------------------------------------------------

cleanup_files() {
    # Remove all file in playground except .gitignore
    find . -mindepth 1 -not -name '.gitignore' -exec rm -rf {} +

    # Remove Q Developer cache
    if [ "$1" == "--hard" -a -d ~/.aws/amazonq/cache/* ]; then
        rm -r ~/.aws/amazonq/cache/*
    fi

    # Remove Q Developer mcp servers
    if [ "$1" == "--hard" -a -f ~/.aws/amazonq/mcp.json ]; then
        save_name="$HOME/.aws/amazonq/mcp.json.$(date +%Y-%m-%d-%H-%M-%S)"
        cp ~/.aws/amazonq/mcp.json $save_name
        rm ~/.aws/amazonq/mcp.json
    fi
}

case "$@" in
    *--hard*)
        cleanup_files --hard
        ;;
    *--no-clear*)
        echo > /dev/null
        ;;
    *mcp-server*)
        cleanup_files --mcp-server
        ;;
    *)
        cleanup_files
        ;;
esac

# -----------------------------------------------------------------------------
# Create starting point configuration
# -----------------------------------------------------------------------------

WITH_RESULT=false

for arg in "$@"; do
    case "$arg" in
        --with-starting-point-folder=*)
            echo > /dev/null
            ;;
        --with-cdk-template)
            cp -r ../../tutorials-starting-points/cdk-template/* .
            ;;
        --with-q-rules)
            cp -r ../../tutorials-starting-points/q-rules/.amazonq .
            ;;
        --with-result)
            WITH_RESULT=true
            ;;
        --with-simplest-mcp-server)
            cp ../../tutorials-starting-points/mcp-servers/mcp-simplest.json ~/.aws/amazonq/mcp.json
            cp ../../tutorials-starting-points/mcp-servers/simplest-mcp-server.py .
            ;;
        --with-diagram-mcp-server)
            cp ../../tutorials-starting-points/mcp-servers/mcp-diagram.json ~/.aws/amazonq/mcp.json
            ;;
        --hard|--no-clear)
            # Skip validation for these known args handled elsewhere
            ;;
        *)
            echo
            echo -e "\033[31m" #Red           
            echo -e "!Error: Invalid argument '$arg'"
            echo -e "Valid arguments are: --with-cdk-template, --with-q-rules, --with-result, --with-simplest-mcp-server, --with-diagram-mcp-server, --hard, --no-clear"
            echo -e "\033[0m"
            echo
            exit 1
            ;;
    esac
done

# -----------------------------------------------------------------------------
# Copy starting point files
# -----------------------------------------------------------------------------

if [ $tutorial_choice == '0' ]; then
set -- "$@" "--with-starting-point-folder=empty"
fi

if [ $tutorial_choice == '1' ]; then
set -- "$@" "--with-starting-point-folder=feedback-app-code"
fi

if [ $tutorial_choice == '1' -a "$WITH_RESULT" == "true" ]; then
set -- "$@" "--with-results=code-generated-from-drawio-diagram/code-generated-from-q-desktop/feedback-app"
fi

if [ $tutorial_choice == '2' ]; then
set -- "$@" "--with-starting-point-folder=feedback-app-diagram"
fi

if [ $tutorial_choice == '2' -a "$WITH_RESULT" == "true" ]; then
set -- "$@" "--with-results=code-generated-from-drawio-diagram/code-generated-from-q-desktop/feedback-app"
set -- "$@" "--with-results=rewritten-diagrams"
fi

if [ $tutorial_choice == '3' ]; then
set -- "$@" "--with-starting-point-folder=s3-notification-diagram"
fi

if [ $tutorial_choice == '3' -a "$WITH_RESULT" == "true" ]; then
set -- "$@" "--with-results=code-generated-from-drawio-diagram/code-generated-from-q-desktop/data-pipeline"
fi

if [ $tutorial_choice == '4' ]; then
set -- "$@" "--with-starting-point-folder=data-pipeline-diagram"
fi

if [ $tutorial_choice == '5' ]; then
set -- "$@" "--with-starting-point-folder=deployment-pipeline"
fi

if [ $tutorial_choice == '6' ]; then
set -- "$@" "--with-starting-point-folder=api-gateway-diagram"
fi

if [ $tutorial_choice == '7' ]; then
set -- "$@" "--with-starting-point-folder=lambda-app-hand-drawn-diagram"
fi

if [ $tutorial_choice == '8' ]; then
set -- "$@" "--with-starting-point-folder=ecs-app-hand-drawn-diagram"
fi

if [ $tutorial_choice == '9' ]; then
set -- "$@" "--with-starting-point-folder=security-pillar-hand-drawn-diagram"
fi

if [ $tutorial_choice == '10' ]; then
set -- "$@" "--with-starting-point-folder=feedback-app-hand-drawn-diagram"
fi

for arg in "$@"; do
    case "$arg" in
        --with-starting-point-folder=*)
            folder="${arg#*=}"
            if [[ "$folder" != "empty" ]]; then
                cp -r ../../tutorials-starting-points/$folder/* . 
            fi
        ;;
        --with-results=*)
            folder="${arg#*=}"
            cp -r ../../tutorials-generated-examples/$folder/* . 
        ;;   
        *)
            echo
            ;;
    esac
done

# -----------------------------------------------------------------------------
# Show Tutorial
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


tutorial_description() {
    if [[ "$1" == *"--with-starting-point-folder=empty"* ]]; then
        clear
        ../show_tutorial_prompts.py '--with-starting-point-folder=empty'
    fi
    if [[ "$1" == *"--with-starting-point-folder=feedback-app-code"* ]]; then
        clear
        ../show_tutorial_prompts.py '--with-starting-point-folder=feedback-app-code'
    fi
    if [[ "$1" == *"--with-starting-point-folder=feedback-app-diagram"* ]]; then
        clear
        ../show_tutorial_prompts.py '--with-starting-point-folder=feedback-app-diagram'
    fi
    if [[ "$1" == *"--with-starting-point-folder=s3-notification-diagram"* ]]; then
        clear
        ../show_tutorial_prompts.py '--with-starting-point-folder=s3-notification-diagram'
    fi
    if [[ "$1" == *"--with-starting-point-folder=data-pipeline-diagram"* ]]; then
        clear
        ../show_tutorial_prompts.py '--with-starting-point-folder=data-pipeline-diagram'
    fi
    if [[ "$1" == *"--with-starting-point-folder=deployment-pipeline"* ]]; then
        clear
        ../show_tutorial_prompts.py '--with-starting-point-folder=deployment-pipeline'
    fi
    if [[ "$1" == *"--with-starting-point-folder=api-gateway-diagram"* ]]; then
        tutorial_description_6
    fi
    if [[ "$1" == *"--with-starting-point-folder=lambda-app-hand-drawn-diagram"* ]]; then
        tutorial_description_7
    fi
    if [[ "$1" == *"--with-starting-point-folder=ecs-app-hand-drawn-diagram"* ]]; then
        tutorial_description_8
    fi
    if [[ "$1" == *"--with-starting-point-folder=security-pillar-hand-drawn-diagram"* ]]; then
        tutorial_description_9
    fi
    if [[ "$1" == *"--with-starting-point-folder=feedback-app-hand-drawn-diagram"* ]]; then
        tutorial_description_10
    fi
}

tutorial_description "$@"