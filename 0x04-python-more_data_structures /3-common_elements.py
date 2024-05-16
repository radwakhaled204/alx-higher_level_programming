#!/usr/bin/python3

def common_elements(set_1, set_2):
    # create an empty set to store the result
    result = set()
    # loop through each element of set_1
    for x in set_1:
        # check if x is also in set_2
        if x in set_2:
            result.add(x)
    return result
