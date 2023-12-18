#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header using the requests and sys
packages
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command line argument
    url = sys.argv[1]
    # Send a GET request to the given URL
    response = requests.get(url)
    # Get the headers of the response as a dictionary
    headers = response.headers
    # Print the value of the X-Request-Id variable
    print(headers.get("X-Request-Id"))
