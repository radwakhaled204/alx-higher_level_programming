#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # loop through each row in the matrix
    for row in matrix:
        # initialize an empty string to store the formated row
        row_string = ""
        # loop element in row
        for element in row:
            row_string += "{:d} ".format(element)
        # print the row without tailing space
        print(row_string[:-1])
