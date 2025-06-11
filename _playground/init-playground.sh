#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

if [[ "$@" =~ "--help" ]]; then
    echo "usage: $0 [--hard] [--no-clear] [--with-cdk-template] [--with-q-rules] [--with-result]"
    exit 0
fi


if ! [[ "$@" =~ "--hard" ]]; then
echo
echo -e "\033[33m-------------------------------------------------------------------------------\033[0m"
echo -e "\033[33m# Refreshing the @workspace index can help when you don't get the expected result\033[0m"
echo -e "\033[33m# If needed, use: '$0 --hard', then Ctrl+Shift+P => 'Developer: Reload Window'\033[0m"
echo -e "\033[33m-------------------------------------------------------------------------------\033[0m"
fi

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

case "$@" in
    *--hard*)
        ../clear-playground.sh --hard
        ;;
    *--no-clear*)
        echo > /dev/null
        ;;
    *mcp-server*)
        ../clear-playground.sh --mcp-server
        ;;
    *)
        ../clear-playground.sh
        ;;
esac

WITH_RESULT=false

for arg in "$@"; do
    case "$arg" in
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

if [ "$WITH_RESULT" = true ]; then
    cp -r ../../tutorials-generated-examples/drawio-diagram-generated-from-code/* .
fi

}

prepare_playground_empty_folder() {

echo
   
}

prepare_playground_feedback_app_diagram() {

cp -r ../../tutorials-starting-points/feedback-app-diagram/* .

if [ "$WITH_RESULT" = true ]; then
    cp -r ../../tutorials-generated-examples/code-generated-from-drawio-diagram/code-generated-from-q-desktop/feedback-app/* .
    cp -r ../../tutorials-generated-examples/rewritten-diagrams/* .
fi
   
}

prepare_playground_s3_notification() {

cp -r ../../tutorials-starting-points/s3-notification-diagram/* .
   
}

prepare_playground_data_pipeline() {

cp -r ../../tutorials-starting-points/data-pipeline-diagram/* .

if [ "$WITH_RESULT" = true ]; then
    cp -r ../../tutorials-generated-examples/code-generated-from-drawio-diagram/code-generated-from-q-desktop/data-pipeline/* .
fi
   
}

prepare_playground_deployment_pipeline() {

cp -r ../../tutorials-starting-points/deployment-pipeline/* .
   
}

prepare_playground_api_gateway() {

cp -r ../../tutorials-starting-points/api-gateway-diagram/* .
   
}

prepare_playground_lambda_app_hand_drawn() {

cp -r ../../tutorials-starting-points/lambda-app-hand-drawn-diagram/* .
   
}

prepare_playground_ecs_app_hand_drawn() {

cp -r ../../tutorials-starting-points/ecs-app-hand-drawn-diagram/* .
   
}

prepare_playground_security_pillar_hand_drawn() {

cp -r ../../tutorials-starting-points/security-pillar-hand-drawn-diagram/* .
   
}

prepare_playground_feedback_gui_hand_drawn() {

cp -r ../../tutorials-starting-points/feedback-app-hand-drawn-diagram/* .
   
}

. ../tutorial_descriptions.sh

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

if [ $tutorial_choice == '6' ]; then
prepare_playground_api_gateway
tutorial_description_6
fi

if [ $tutorial_choice == '7' ]; then
prepare_playground_lambda_app_hand_drawn
tutorial_description_7
fi

if [ $tutorial_choice == '8' ]; then
prepare_playground_ecs_app_hand_drawn
tutorial_description_8
fi

if [ $tutorial_choice == '9' ]; then
prepare_playground_security_pillar_hand_drawn
tutorial_description_9
fi

if [ $tutorial_choice == '10' ]; then
prepare_playground_feedback_gui_hand_drawn
tutorial_description_10
fi
