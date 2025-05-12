#!/bin/bash

# Verify q cli is not installed or version is too old
if [ $(which q) ]; then
    version=$(q --version | cut -d' ' -f2)
    if [ "$(printf '%s\n' "1.9.1" "$version" | sort -V | head -n1)" = "$version" -a "$version" != "1.9.1" ]; then        
        echo "q cli version $version is too old. Replacing with newest version"
    else
        echo "q cli is already installed"
        exit
    fi
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
