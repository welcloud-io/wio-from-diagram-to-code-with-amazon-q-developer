#!/bin/bash

# Verify q cli is not installed or version is too old
if [ $(which q) ]; then
    version=$(q --version | cut -d' ' -f2)
    minimum_version="1.12.1"
    if [ "$(printf '%s\n' "$minimum_version" "$version" | sort -V | head -n1)" = "$version" -a "$version" != "$minimum_version" ]; then        
        echo "q cli version ($version) is too old. Replacing with minimum version ($minimum_version)"
    else
        echo "q cli minimum version $version is already installed"
        exit
    fi
fi

# Ask for confiramtion
read -p "Do you want to proceed with Amazon Q ($minimum_version) installation (Yes/no)? " confirmation

if [ "$confirmation" != "Yes" ]; then
    exit
fi

# Install Q CLI
echo "Download Amazon Q CLI Ubuntu package"
wget https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb
sudo apt install -y ./amazon-q.deb
rm  ./amazon-q.deb

# Propose Q Login
q login
