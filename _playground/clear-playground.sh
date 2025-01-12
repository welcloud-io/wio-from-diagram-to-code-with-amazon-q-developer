# Empty application folder
cd "$(dirname "$0")"
cd vscode-app-folder

find . ! -name '.gitignore' -type f -exec rm -f {} +

# Empty @worksapce cache folder if not empty already
if [ -z "$(ls -A ~/.aws/amazonq/cache/cache)" ]; then
    echo "Cache folder is empty"
else
    echo "Cache folder is not empty"
    # remove all files in cache folder
    rm ~/.aws/amazonq/cache/cache/*
fi