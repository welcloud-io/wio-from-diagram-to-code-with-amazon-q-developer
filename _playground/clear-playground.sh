#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

# Remove all file in playground except .gitignore
find . -mindepth 1 -not -name '.gitignore' -exec rm -rf {} +

# Save and remove mcp.json
mkdir -p /tmp/saved-mcp-server-json
cp ~/.aws/amazonq/mcp.json /tmp/saved-mcp-server-json/mcp.json.$(date +%Y%m%d_%H%M%S)
rm ~/.aws/amazonq/mcp.json

# Remove Q Developer cache
if [ "$1" == "--hard" ]; then
    rm ~/.aws/amazonq/cache/cache/*
fi