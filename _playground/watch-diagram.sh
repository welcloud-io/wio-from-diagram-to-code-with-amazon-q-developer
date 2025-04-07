#!/bin/bash

q chat --accept-all "generate application"

while inotifywait -e modify diagram.drawio; do
    echo "File changed, executing command..."
    q chat --accept-all "generate application"
done