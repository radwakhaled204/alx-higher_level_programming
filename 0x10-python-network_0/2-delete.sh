#!/bin/bash
# This script takes a URL as an argument and sends a DELETE request to that URL and displays the body of the response
curl -sX DELETE "$1"
