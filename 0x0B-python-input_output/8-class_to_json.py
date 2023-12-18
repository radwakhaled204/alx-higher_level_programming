#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure for JSON serialization of an object

    Args:
        obj (any): An instance of a Class

    Returns:
        dict: The dictionary representation of the object's attributes
    """
    # Use the built-in __dict__ attribute to
    # get the dictionary of the object's attributes
    return obj.__dict__
