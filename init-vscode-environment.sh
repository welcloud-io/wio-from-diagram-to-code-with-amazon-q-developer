exit

# Install plugins
code --install-extension bierner.markdown-mermaid
code --install-extension amazonwebservices.amazon-q-vscode
code --install-extension hediet.vscode-drawio

# Setup settings
cat << 'EOF' > ~/config/Code/User/settings.json
{
    "amazonQ.workspaceIndex": true,
    "workbench.editorAssociations": {
        "*.drawio.xml": "hediet.vscode-drawio-text"
    }
}
EOF