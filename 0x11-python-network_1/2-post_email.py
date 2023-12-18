#!/usr/bin/python3
"""
This module takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded
in utf-8) using the urllib and sys packages
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Get the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # Encode the email as a parameter in a dictionary
    data = urllib.parse.urlencode({'email': email})
    # convert the data to bytes
    data = data.encode('ascii')
    # Create a request object with the URL and data
    req = urllib.request.Request(url, data)
    # Open the request object and read the response
    with urllib.request.urlopen(req) as response:
        # Decode the response body as utf-8
        html = response.read().decode('utf-8')
        # Print the response body
        print(html)
