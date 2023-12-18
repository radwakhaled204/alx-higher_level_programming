#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response
using the urllib and sys packages
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL from the command line argument
    url = sys.argv[1]
    # Open a request object with the given URL
    with urllib.request.urlopen(url) as response:
        # Get the headers of the response as a dictionary
        headers = response.info()
        # Print the value of the X-Request-Id variable
        print(headers.get("X-Request-Id"))
