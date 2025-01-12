cd "$(dirname "$0")"
cd vscode-app-folder

../clear-playground.sh $1

# Display available tutorials
echo "Available tutorials:"
echo "1. From code to diagram with Mermaid"
echo "2. From diagram to code with Mermaid"
echo "3. From diagram to code with draw.io"
echo "4. From code to diagram with draw.io"

# Prompt user to select tutorial
read -p "Which tutorial would you like to view? (1-4): " tutorial_choice

# Validate input
if [[ ! $tutorial_choice =~ ^[1-5]$ ]]; then
    echo "Invalid selection. Please choose a number between 1 and 5."
    exit 1
fi

if [ $tutorial_choice == '1' ]; then
echo "preparing playground for tutorial $tutorial_choice..."
cp -r ../../tutorials-starting-points/feedback-app-code/* .
cat << 'EOF' > MERMAID-DIAGRAMS.md
```mermaid
<PUT MERMAID CODE HERE AND CLICK ON PREVIEW AT THE RIGHT HAND CORNER>
```
EOF
echo "Done."
echo "Created files:"
ls
fi

if [ $tutorial_choice == '2' ]; then
echo "preparing playground for tutorial $tutorial_choice..."
echo "Done."
echo "Folder should be empty"
ls
fi

if [ $tutorial_choice == '3' ]; then
echo "preparing playground for tutorial $tutorial_choice..."
cp -r ../../tutorials-starting-points/feedback-app-diagram/* .
echo "Done."
echo "Created files:"
ls
fi

if [ $tutorial_choice == '4' ]; then
echo "preparing playground for tutorial $tutorial_choice..."
cp -r ../../tutorials-starting-points/feedback-app-code/* .
echo "Done."
echo "Created files:"
ls
fi
