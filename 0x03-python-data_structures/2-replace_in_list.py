#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    # otherwise replace the element
    my_list[idx] = element
    return my_list
