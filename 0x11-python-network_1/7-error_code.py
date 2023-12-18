#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the body of
the response using the requests and sys packages.
It also checks the HTTP status code and prints
an error message if it is greater than or equal to 400.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command line argument
    url = sys.argv[1]
    # Send a GET request to the given URL
    response = requests.get(url)
    # Get the HTTP status code
    status = response.status_code
    # Check if the status code is greater than or equal to 400
    if status >= 400:
        # Print an error message with the status code
        print("Error code: {}".format(status))
    else:
        # Get the response body as a string
        html = response.text
        # Print the response body
        print(html)
