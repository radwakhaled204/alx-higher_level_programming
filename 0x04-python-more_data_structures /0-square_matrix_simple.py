#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # create a new matrix to store result
    new_matrix = []

    # loop through each row in matrix
    for row in matrix:
        # create a new row to store squared values
        new_row = []
        # loop through each element of the row
        for x in row:
            # square element and append it to new_row
            new_row.append(x ** 2)
        new_matrix.append(new_row)
    return new_matrix
