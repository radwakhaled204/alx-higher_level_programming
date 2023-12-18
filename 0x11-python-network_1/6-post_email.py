#!/usr/bin/python3
"""
This module takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
using the requests and sys packages
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL and email address from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # Send a POST request to the given URL with the email as a parameter
    response = requests.post(url, data={'email': email})
    # Get the response body as a string
    html = response.text
    # Print the response body
    print(html)
