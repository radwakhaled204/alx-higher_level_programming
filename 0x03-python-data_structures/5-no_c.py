#!/usr/bin/python3

def no_c(my_string):
    # initialize and empty string to store result
    new_string = ""
    # loop through the string
    for i in my_string:
        if i not in "cC":
            new_string += i
    return new_string
