#!/bin/bash -e

cd "$(dirname "$0")"
cd vscode-app-folder

if [[ "$@" =~ "--help" ]]; then
    echo "usage: $0 [--hard] [--no-clear] [--with-starting-point-folder=<folder_name>] [--with-mcp-server=<mcp-json-file>] [--with-q-rules]"
    exit 0
fi

# -----------------------------------------------------------------------------
# Choose tutorial configurtaion 
# -----------------------------------------------------------------------------

if ! [[ "$@" =~ "--with-starting-point-folder=" || "$@" =~ "--with-result-folder=" ]]; then

    # Map of tutorial choices to folder names
    declare -A tutorial_map=(
        [0]="empty"
        [1]="feedback-app-code" 
        [2]="feedback-app-diagram"
        [3]="s3-notification-diagram"
        [4]="data-pipeline-diagram"
        [5]="deployment-pipeline"
        [6]="api-gateway-diagram"
        [7]="lambda-app-hand-drawn-diagram"
        [8]="ecs-app-hand-drawn-diagram"
        [9]="security-pillar-hand-drawn-diagram"
        [10]="feedback-app-hand-drawn-diagram"
        [11]="layered-architecture-diagram"
        [12]="strands-ai-agent-diagram-and-rules"
    )

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
        echo "11. Layered Architecture (from AWS Diagram to C4 Model)"
        echo "12. Strands AI Agent (From Drawio Diagram to code)"
        echo

        # Prompt user to select tutorial
        read -p "Where do you want to start from ?: " tutorial_choice

        # Validate input
        if [[ ! $tutorial_choice =~ ^[0-9]$|^1[0-2]$ ]]; then    
            echo "Invalid selection. Please choose a number between 0 and 10."
            exit 1
        fi
    fi

    # Set starting point folder based on selection
    set -- "$@" "--with-starting-point-folder=${tutorial_map[$tutorial_choice]}"

    if [[ "$@" =~ "--with-result" ]]; then
        set -- "$@" "--with-result-folder=${tutorial_map[$tutorial_choice]}"
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

for arg in "$@"; do
    case "$arg" in
        --with-starting-point-folder=*)
            folder="${arg#*=}"
            if [[ "$folder" != "empty" ]]; then
                cp -r ../../tutorials/tutorial-starting-points/$folder/* . 
                cp -r ../../tutorials/tutorial-starting-points/$folder/.amazonq* . 
            fi
        ;;
        --with-result)
            # No action - a folder is assigned at tutorial choice
        ;;
        --with-result-folder=*)
            folder="${arg#*=}"
            if [[ "$folder" != "empty" ]]; then
                cp -r ../../tutorials/tutorial-generated-examples/$folder/* . 
                cp -r ../../tutorials/tutorial-starting-points/$folder/.amazonq* .
            fi
        ;;
        --with-q-rules)
            cp -r ../../tutorials/tutorial-starting-points/q-rules/.amazonq .
            ;;
        --with-mcp-server=*)
            mcp_json_file="${arg#*=}"
            cp ../../tutorials/tutorial-starting-points/mcp-servers/$mcp_json_file ~/.aws/amazonq/mcp.json
            if [ -f "../../tutorials/tutorial-starting-points/mcp-servers/${mcp_json_file%.json}.py" ]; then
                cp ../../tutorials/tutorial-starting-points/mcp-servers/${mcp_json_file%.json}.py .
            fi                        
        ;;
        --hard|--no-clear)
            # Skip validation for these known args handled elsewhere
            ;;
        *)
            echo
            echo -e "\033[31m" #Red           
            echo -e "!Error: Invalid argument '$arg'"
            echo -e "Valid arguments are: --hard, --no-clear, --with-q-rules, --with-starting-point-folder=<folder_name>, --with-starting-point-folder=<folder_name>, --with-mcp-server=<mcp-json-file>"
            echo -e "\033[0m"
            echo
            exit 1
            ;;
    esac
done

# -----------------------------------------------------------------------------
# Copy starting point files
# -----------------------------------------------------------------------------

clear
../../tutorials/show_tutorial_prompts.py "$@"
