#!/bin/bash
# This script takes a URL and a filename as arguments and sends a JSON POST request to the URL with the contents of the file and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
