#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
using the requests package
"""

import requests

if __name__ == "__main__":
    # Send a GET request to the given URL
    response = requests.get('https://alx-intranet.hbtn.io/status')
    # Get the response body as a string
    html = response.text
    # Print the body response
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
