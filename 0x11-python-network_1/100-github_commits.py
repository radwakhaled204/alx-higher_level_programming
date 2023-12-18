#!/usr/bin/python3
"""
This module takes a repository name and an owner name and lists 10 commits
(from the most recent to oldest) of the repository by the user, using the
GitHub API and the requests package.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the repository name& the owner name from the command line arguments
    repo = sys.argv[1]
    owner = sys.argv[2]
    # Set the URL for the GitHub API with the given parameters
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    # Send a GET request to the URL
    response = requests.get(url)
    # Get the JSON data from the response
    commits = response.json()
    # Try to loop through the first 10 items of the data
    try:
        for i in range(10):
            # Print the sha and the author name for each commit
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    # Handle the exception if the data has less than 10 items
    except IndexError:
        pass
