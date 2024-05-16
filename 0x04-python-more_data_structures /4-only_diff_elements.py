#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # create an empty set to store result
    result = set()

    # loop through each element of set_1
    for x in set_1:
        # check if x is not in set_2
        if x not in set_2:
            result.add(x)
    # loop through each element of set_2
    for x in set_2:
        # check if x is not in set_1
        if x not in set_1:
            result.add(x)
    return result
