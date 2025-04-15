#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

if [[ "$@" =~ "--help" ]]; then
    echo "usage: $0 [--hard] [--no-clear] [--with-cdk-template] [--with-q-rules] [--with-result]"
    exit 0
fi

echo
echo "Available starting points:"
echo
echo "0. Empty Folder (from Code to Diagram)"
echo "1. Feedback App Code (from Code to Diagram)"
echo "2. Feedback App Diagram (from Diagram to Code)"
echo "3. S3 notification (from Diagram to Code)"
echo "4. Data pipeline (from Diagram to Code)"
echo "5. Deployment pipeline (from Diagram to Code)"
echo "6. Api Gateway (from Diagram to Code)"
echo

# Prompt user to select tutorial
read -p "Where do you want to start from (0-6)?: " tutorial_choice

# Validate input
if [[ ! $tutorial_choice =~ ^[0-6]$ ]]; then
    echo "Invalid selection. Please choose a number between 0 and 5."
    exit 1
fi

if [[ "$@" =~ "--hard" ]]; then
    ../clear-playground.sh --hard
else
    if [[ "$@" =~ "--no-clear" ]]; then
        echo > /dev/null
    else
        ../clear-playground.sh
    fi
fi

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

}

prepare_playground_empty_folder() {

echo
   
}

prepare_playground_feedback_app_diagram() {

cp -r ../../tutorials-starting-points/feedback-app-diagram/* .

if [ "$WITH_RESULT" = true ]; then
    cp -r ../../tutorials-generated-examples/code-generated-from-drawio-diagram/code-generated-from-q-desktop/feedback-app/* .
fi
   
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

prepare_playground_api_gateway() {

cp -r ../../tutorials-starting-points/api-gateway-diagram/* .
   
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

