#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


# Define a function that takes two parameters: a matrix and a divisor
def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """

    # Initialize an empty list to store the result matrix
    divided_matrix = []

    # Raise a TypeError if div is not a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Raise a ZeroDivisionError if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Loop through each row of the matrix
    for row in matrix:
        # Raise a TypeError if the row length is not consistent
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        # Initialize an empty list to store the divided row
        divided_row = []
        # Loop through each element of the row
        for element in row:
            # Raise a TypeError if the element is not an int or a float
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            else:
                # Divide the element by div and round it to two decimal places
                divided_row.append(round(element / div, 2))
        # Append the divided row to the result matrix
        divided_matrix.append(divided_row)

    # Return the result matrix
    return divided_matrix
