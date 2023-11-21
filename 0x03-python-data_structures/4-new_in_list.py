#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # create a copy of the original list
    new_list = my_list[:]
    # check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element
    return new_list
