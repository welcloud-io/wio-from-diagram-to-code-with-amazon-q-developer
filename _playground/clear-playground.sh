#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

# Remove all file in playground except .gitignore
find . -mindepth 1 -not -name '.gitignore' -exec rm -rf {} +

# if mcp.json exists
if [ -f ~/.aws/amazonq/mcp.json ]; then
    cp ~/.aws/amazonq/mcp.json ~/.aws/amazonq/mcp.json.$(date +%Y%m%d_%H:%M:%S)
    rm ~/.aws/amazonq/mcp.json
fi

# Remove Q Developer cache
if [ "$1" == "--hard" ]; then
    rm ~/.aws/amazonq/cache/cache/*
fi