#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # create an empty list to store the result
    result = []
    # loop through the original list
    for i in my_list:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
