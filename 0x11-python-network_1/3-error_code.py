#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8) using the urllib and sys packages. It also
manages urllib.error.HTTPError exceptions and prints the error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # get the url from the command line argument
    url = sys.argv[1]
    # try to open a request with the given url
    try:
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            html = response.read().decode('utf-8')
            # print the response body
            print(html)
    # handle the htttperror expecion
    except urllib.error.HTTPError as e:
        # print the error code
        print("Error code: {}".format(e.code))
