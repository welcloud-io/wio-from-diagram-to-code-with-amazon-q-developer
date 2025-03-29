cd "$(dirname "$0")"
cd vscode-app-folder

# Display available tutorials
echo "Available tutorials:"
echo "1. From code to diagram with Mermaid"
echo "2. From diagram to code with Mermaid"
echo "3. From diagram to code with draw.io"
echo "4. From code to diagram with draw.io"
echo "5. More..."

# Prompt user to select tutorial
read -p "Which tutorial would you like to view? (1-5): " tutorial_choice

# Validate input
if [[ ! $tutorial_choice =~ ^[1-5]$ ]]; then
    echo "Invalid selection. Please choose a number between 1 and 5."
    exit 1
fi

if [ $tutorial_choice != '5' ]; then
   ../clear-playground.sh $1
fi

if [ $tutorial_choice == '1' ]; then
echo """
-------------------------------------------------------------------------------
"""
echo "preparing playground for tutorial $tutorial_choice..."
cp -r ../../tutorials-starting-points/feedback-app-code/* .
cat << 'EOF' > MERMAID-DIAGRAMS.md
```mermaid
<PUT MERMAID CODE HERE AND CLICK ON PREVIEW AT THE RIGHT HAND CORNER>
```
EOF
cat << 'EOF' > APP.DRAWIO.XML
<PUT GENERATED DIAGRAM HERE>
EOF
echo "Done."
echo "Created files:"
ls -1
echo """
-------------------------------------------------------------------------------
$(tput bold)$(tput setaf 2)[From Code to Mermaid Diagram with Q Desktop] PROMPTS:$(tput sgr0)

...Go to Q Desktop en enter

$(tput bold)> @workspace can you generate a mermaid diagram of my application$(tput sgr0)

...Copy/Paste prompt results in MERMAID-DIAGRAMS.md

$(tput bold)> @workspace can you generate a mermaid sequence diagram of the application$(tput sgr0)

...Copy/Paste prompt results in MERMAID-DIAGRAMS.md

$(tput bold)> @workspace can you generate a mermaid class diagram of the application$(tput sgr0)

...Copy/Paste prompt results in MERMAID-DIAGRAMS.md

-------------------------------------------------------------------------------
$(tput bold)$(tput setaf 2)[From Code to Drawio Diagram with Q Desktop] PROMPTS:$(tput sgr0)

...Go to Q Desktop and enter

$(tput bold)> @workspace generate a draw.io diagram in an xml format for this application (I want to use AWS 2024 Icons, lines should be orthogonal, dataflow from up to bottom)$(tput sgr0) 

...Copy/Paste prompt results in APP.DRAWIO.XML (Open it with text editor)

-------------------------------------------------------------------------------
"""
fi

if [ $tutorial_choice == '2' ]; then
echo """
-------------------------------------------------------------------------------
"""
echo "preparing playground for tutorial $tutorial_choice..."
echo "Done."
echo "Folder should be empty"
ls -l
echo """
-------------------------------------------------------------------------------
$(tput bold)$(tput setaf 2)[From Mermaid Diagram to Code with Q Desktop] PROMPTS:$(tput sgr0)

...Go to Q Desktop and enter

$(tput bold)> /dev can you generate application files from this mermaid diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)
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
end$(tput sgr0)

...Deploy generated code in your folder with 'cdk deploy'
-------------------------------------------------------------------------------
"""
fi

if [ $tutorial_choice == '3' ]; then
echo """
-------------------------------------------------------------------------------
"""
echo "preparing playground for tutorial $tutorial_choice..."
cp -r ../../tutorials-starting-points/feedback-app-diagram/* .
echo "Done."
echo "Created files:"
ls -1
echo """
-------------------------------------------------------------------------------
$(tput bold)$(tput setaf 2)[From Drawio Diagram to Code with Q Desktop] PROMPTS:$(tput sgr0)

...Open drawio diagram in folder

...Go to Q Desktop and enter

$(tput bold)> /dev can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)$(tput sgr0)

...Deploy generated code in your folder with 'cdk deploy'

-------------------------------------------------------------------------------
$(tput bold)$(tput setaf 2)[From Drawio Diagram to Code with Q CLI] PROMPTS:$(tput sgr0)

...Open terminal and type:
$> q chat

$(tput bold)> can you generate application from the drawio diagram (I want the code of the lambdas to be written in python and the infrastructure as code with the python cdk v2)$(tput sgr0)

...Say yes (y) to all

$(tput bold)> modify the drawio diagram to split the architecture diagram into well defined cdk construts (use colors and legend)$(tput sgr0)

...Say yes (y) to all

...Deploy generated code in your folder with 'cdk deploy'

-------------------------------------------------------------------------------
"""
fi

if [ $tutorial_choice == '4' ]; then
echo "preparing playground for tutorial $tutorial_choice..."
cp -r ../../tutorials-starting-points/feedback-app-code/* .
cat << 'EOF' > app.drawio.xml
<PUT GENERATED DIAGRAM HERE>
EOF
echo "Done."
echo "Created files:"
ls -l
echo """

"""
fi

if [ $tutorial_choice == '5' ]; then
echo
echo "More..."
../init-playground-more.sh
fi
