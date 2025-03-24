#!/bin/bash

# Verify q cli is not istalled
if [ $(which q) ]; then
    echo "q cli is already installed"
    exit
fi

# Ask for confiramtion
echo "Should work on Ubuntu 22.04"
read -p "Do you want to proceed with Amazon Q installation (Yes/no)? " confirmation

if [ "$confirmation" != "Yes" ]; then
    exit
fi

# Install Q CLI
curl --proto '=https' --tlsv1.2 -sSf https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb -o amazon-q.deb
sudo apt install -y ./amazon-q.deb
rm  ./amazon-q.deb

# Propose Q Login
q login