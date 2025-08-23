#!/bin/bash

# Install plugins
code --install-extension bierner.markdown-mermaid
code --install-extension amazonwebservices.amazon-q-vscode
code --install-extension hediet.vscode-drawio

# Setup settings
# Only execute if the file doesn't exist to avoid overwrite existing settings
echo
echo "Create settings"
if [ ! -f ~/.config/Code/User/settings.json ]; then
mkdir -p ~/.config/Code/User
cat << 'EOF' > ~/.config/Code/User/settings.json
{
    "amazonQ.workspaceIndex": true,
    "workbench.editorAssociations": {
        "*.drawio.xml": "hediet.vscode-drawio-text"
    }
}
EOF
else
echo "! Settings file (~/.config/Code/User/settings.json) already exists"
echo "! Please create settings manually to avoid overwrite. c.f. ./README.md"
fi
