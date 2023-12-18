#!/usr/bin/python3
"""
This a script return the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    This function returns the list of attributes and methods of and obj

    Args:
        obj: The object to get the attributes and methods for.

    Returns:
        A list containing the names of the attributes and methods of the object
    """
    # create an empty list to store attributes of the object.
    names = []
    # loop through the names of in the object
    for name in dir(obj):
        # append the name to the list
        names.append(name)
    # return the list of names
    return names
