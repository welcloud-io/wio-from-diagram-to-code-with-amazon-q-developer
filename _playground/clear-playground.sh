#!/bin/bash

cd "$(dirname "$0")"
cd vscode-app-folder

find . -mindepth 1 -not -name '.gitignore' -exec rm -rf {} +

if [ "$1" == "--hard" ]; then
    rm ~/.aws/amazonq/cache/cache/*
fi