#!/usr/bin/python3
"""returns an object (Python data structure) represented by a JSON string"""


# Import the json module
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The Python object represented by the JSON string.
    """
    # Use the json.loads() function to convert the
    # JSON string to a Python object
    return json.loads(my_str)
