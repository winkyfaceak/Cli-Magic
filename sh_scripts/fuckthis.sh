#!/bin/bash

# Check if the argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <path>"
    exit 1
fi
# Check if the argument is a directory
if [ -d "$1" ]; then
   sudo rm -d -r "$1"
# Check if the argument is a regular file
elif [ -f "$1" ]; then
    sudo rm "$1"
# If the argument is neither a directory nor a regular file
else
    echo "$1 is not a valid directory or file."
fi