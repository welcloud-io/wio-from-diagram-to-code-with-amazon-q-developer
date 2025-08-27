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

clear
../show_tutorial_prompts.py "$@"