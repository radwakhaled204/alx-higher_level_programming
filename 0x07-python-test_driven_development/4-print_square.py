#!/usr/bin/python3
""" print_square prints a square depending on the "size" parameter
"""


# Define a function that takes one parameter: the size of the square
def print_square(size):
    """ Prints a square with a size
    checks if "size" is an int
    checks if "size" is a float and less than 0
    checks if "size" is less than 0
    checks if "size" is equal to 0
    """

    # Raise a TypeError if size is not an int
    if type(size) != int:
        raise TypeError("size must be an integer")

    # Raise a TypeError if size is a float and less than 0
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    # Raise a ValueError if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Return None if size is equal to 0
    if size == 0:
        return None

    # Loop through each row of the square
    for row in range(size):
        # Print the row with '#' characters repeated by size times
        print('#' * size)
