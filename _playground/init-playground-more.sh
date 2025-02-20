cd "$(dirname "$0")"
cd vscode-app-folder

../clear-playground.sh $1

# Display available tutorials
echo "Available tutorials:"
echo "1. S3 notification (from diagram to code)"
echo "2. Data pipeline (from diagram to code)"
echo "3. Deployment pipeline (from diagram to code)"

# Prompt user to select tutorial
read -p "Which tutorial would you like to view? (1-3): " tutorial_choice

# Validate input
if [[ ! $tutorial_choice =~ ^[1-3]$ ]]; then
    echo "Invalid selection. Please choose a number between 1 and 3."
    exit 1
fi

if [ $tutorial_choice == '1' ]; then
echo "preparing playground for tutorial $tutorial_choice..."
cp -r ../../tutorials-starting-points/s3-notification-diagram/* .
echo "Done."
echo "Created files:"
ls
fi

if [ $tutorial_choice == '2' ]; then
echo
fi

if [ $tutorial_choice == '3' ]; then
echo
fi