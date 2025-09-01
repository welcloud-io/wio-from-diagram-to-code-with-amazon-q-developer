#!/bin/bash

echo "--------------------"
echo "INSTALLING MCP UTILS"
echo "--------------------"

# Install uv for remote MCP servers usage (if not installed yet)
if [ $(which uv) ]; then
    echo "uv is already installed (used for MCP servers)"
else
    echo "Installing uv to use remote MCP servers.."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Install fastmcp for MCP servers usage (if not installed yet)
if [ $(which fastmcp) ]; then
    echo "fastmcp is already installed (used for MCP servers)"
else
    echo "Installing fastmcp to use remote MCP servers.."
    pip install fastmcp
fi
