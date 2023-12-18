#!/usr/bin/python3
"""
this module fetches https://alx-intranet.hbtn.io/status
using the urllib package
"""

import urllib.request

if __name__ == "__main__":
    # Open a request object with the given URL
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status'
            ) as response:
        # read the response body as bytes
        html = response.read()
        # decode the bytes to get a string
        html_str = html.decode('utf-8')
        # print the body response
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html_str))
