#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

# Remove all file in playground except .gitignore
find . -mindepth 1 -not -name '.gitignore' -exec rm -rf {} +

# if mcp.json exists
if [ -f ~/.aws/amazonq/mcp.json -a "$1" == "--mcp-server" ]; then

    save_name="~/.aws/amazonq/mcp.json.$(date +%Y-%m-%d-%H-%M-%S)"
    echo ""
    echo "~/.aws/amazonq/mcp.json exists and will be replaced"
    read -p "Do you want to save it as $save_name? (y/n) " answer

    if [ "$answer" != "${answer#[Yy]}" ] ;then
        echo "Saving file $save_name"
        cp ~/.aws/amazonq/mcp.json $save_name
    fi

    rm ~/.aws/amazonq/mcp.json
fi

# Remove Q Developer cache
if [ "$1" == "--hard" ]; then
    rm ~/.aws/amazonq/cache/cache/*
    save_name="~/.aws/amazonq/mcp.json.$(date +%Y-%m-%d-%H-%M-%S)"
    cp ~/.aws/amazonq/mcp.json $save_name
    rm ~/.aws/amazonq/mcp.json
fi

# Remove Q Developer mcp servers
if [ "$1" == "--hard" ]; then
    save_name="~/.aws/amazonq/mcp.json.$(date +%Y-%m-%d-%H-%M-%S)"
    cp ~/.aws/amazonq/mcp.json $save_name
    rm ~/.aws/amazonq/mcp.json
fi
