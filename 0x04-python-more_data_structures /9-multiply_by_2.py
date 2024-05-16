#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # create new dictionary to store result
    new_dictionary = {}
    # loop through each key/value pair in original dictionary
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
