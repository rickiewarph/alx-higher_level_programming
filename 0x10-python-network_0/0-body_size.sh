#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and get the size of the body in bytes
size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

# Check if size is not empty
if [ -z "$size" ]; then
    echo "Error: Unable to get the size of the body."
    exit 1
fi

echo "$size"
