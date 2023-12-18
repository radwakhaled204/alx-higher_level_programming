#!/usr/bin/python3
"""
This module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter using the
requests and sys packages. It also displays the id and name of the user
found or an error message if the response is not valid or empty.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the letter from the command line argument or set it to empty string
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    # Send a POST request to the given URL with the letter as a parameter
    response = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': letter}
            )
    # Try to get the JSON data from the response
    try:
        data = response.json()
        # Check if the data is empty
        if not data:
            # Print no result message
            print("No result")
        else:
            # Print the id and name of the user found
            print("[{}] {}".format(data.get('id'), data.get('name')))
    # Handle the exception if the response is not valid JSON
    except ValueError:
        # Print not a valid JSON message
        print("Not a valid JSON")
