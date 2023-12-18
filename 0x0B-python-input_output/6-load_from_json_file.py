#!/usr/bin/python3
"""that creates an Object from a “JSON file"""


# Import the json module
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”

    Args:
        filename (str): The name of the file to read from

    Returns:
        any: The object created from the JSON string
    """
    # Open the file in read mode with utf-8 encoding
    with open(filename, "r", encoding="utf-8") as f:
        # Use json.load to parse the JSON string and return the object
        return json.load(f)
