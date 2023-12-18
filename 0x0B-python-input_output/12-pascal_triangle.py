#!/usr/bin/python3
"""returns a list of lists of integers representing Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle of n

    Args:
        n (int): The number of rows of the triangle

    Returns:
        list of list of int: The Pascal’s triangle of n
    """
    # Returns an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Loop from the second row to the nth row
    for i in range(1, n):
        # Initialize the current row with the first element 1
        row = [1]
        # Loop from the second element to the second last element
        for j in range(1, i):
            # The crrent element is the sum of
            # the previous row's adjacent elementsi
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # Append the last element 1 to the current row
        row.append(1)
        # Append the current row to the triangle
        triangle.append(row)

    # Return the triangle
    return triangle
