#!/usr/bin/python3
"""
This module takes your GitHub credentials (username and password) and uses the
GitHub API to display your id using the requests and sys packages. It uses
Basic Authentication with a personal access token as password to access your
information (only read:user permission is needed).
"""

import requests
import sys

if __name__ == "__main__":
    # Get the username and password from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    # Set the URL for the GitHub API
    url = 'https://api.github.com/user'
    # Send a GET request to the URL with the credentials
    response = requests.get(url, auth=(username, password))
    # Get the JSON data from the response
    data = response.json()
    # Print the id of the user or None if not found
    print(data.get('id'))
