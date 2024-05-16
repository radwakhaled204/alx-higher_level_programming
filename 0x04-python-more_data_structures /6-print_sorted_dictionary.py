#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # use sorted function to get list of alphabetic order
    sorted_keys = sorted(a_dictionary.keys())
    # loop through each key in the sorted list
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
