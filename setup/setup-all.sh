#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

"$DIR"/setup-vscode.sh 
"$DIR"/install-mcp-utils.sh  
"$DIR"/install-docker.sh  
"$DIR"/install-q-cli.sh  