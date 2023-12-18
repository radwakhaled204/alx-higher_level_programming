#!/usr/bin/python3
"""This a script adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        obj (object): The object to add the attribute to.
        name (str): The name of the attribute to add.
        value (any): The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    # Check if the object has a __dict__ attribute that
    # allows adding new attributes
    if hasattr(obj, "__dict__"):
        # Set the new attribute with the given name and value
        setattr(obj, name, value)
    else:
        # Raise a TypeError exception with the message can't add new attribute
        raise TypeError("can't add new attribute")
