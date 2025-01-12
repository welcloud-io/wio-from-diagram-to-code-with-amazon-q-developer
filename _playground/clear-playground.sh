# Empty application folder
cd "$(dirname "$0")"
cd vscode-app-folder

find . -not -name '.gitignore' -delete
echo "All files deleted in vscode-app-folder"

if [ "$1" == "--hard" ]; then
    # Empty @worksapce cache folder if not empty already
    if [ -z "$(ls -A ~/.aws/amazonq/cache/cache)" ]; then
        echo "Amazo Q Cache folder is already empty"
    else
        echo "Amazo Q Cache folder is not empty"
        rm ~/.aws/amazonq/cache/cache/*
    fi
fi