#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""


# Import the json module
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (any): The object to be serialized
        filename (str): The name of the file to write to
    """
    # Open the file in write mode with utf-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        # Use json.dump to write the object as a JSON string
        json.dump(my_obj, f)
