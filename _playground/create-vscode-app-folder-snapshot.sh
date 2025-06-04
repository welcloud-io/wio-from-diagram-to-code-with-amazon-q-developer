# /bin/bash

# Create ../../vscode-app-folder-snapshots/ if it does not exist yet
if [ ! -d "../../vscode-app-folder-snapshots" ]; then
  mkdir ../../vscode-app-folder-snapshots
fi

# Create new folder
timestamp=$(date +%Y-%m-%d-%H-%M-%S)
folder_name="snapshot-$timestamp"
mkdir ../../vscode-app-folder-snapshots/$folder_name

# Copy content
cp -r ./* ../../vscode-app-folder-snapshots/$folder_name