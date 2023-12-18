#!/bin/bash
# this script takes a URL as an argument and displays the body of the response if the status code is 200
curl -sL "$1"
