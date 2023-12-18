#!/usr/bin/python3
""" say_my_name prints back the parameters
first_name followed by last_name
last_name is defaulted to an empty string
"""


# Define a function that takes two parameters: a first name and a last name
def say_my_name(first_name, last_name=""):
    """ Prints "My name is <first name> <last name>"
    checks if first_name is a string
    checks if last_name is a string
    """

    # Raise a TypeError if first_name is not a string
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    # Raise a TypeError if last_name is not a string
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    # Format and print the message with the names
    message = "My name is {:s} {:s}".format(first_name, last_name)
    print(message)
