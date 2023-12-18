#!/usr/bin/python3
"""returns the JSON representation of an object"""


# Import the json module
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The object to serialize.

    Returns:
        str: The JSON string of the object.
    """
    # Use the json.dumps() function to convert the object to a JSON string
    return json.dumps(my_obj)
