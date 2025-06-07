#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

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
