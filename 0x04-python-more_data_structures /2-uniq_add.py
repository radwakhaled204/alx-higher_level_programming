#!/usr/bin/python3

def uniq_add(my_list=[]):
    # create a set to store the unique element
    unique_set = set()
    # loop through each element of the list
    for x in my_list:
        # add the element to the set - the duplicate will be ingored
        unique_set.add(x)
    # create variable to store sum
    total = 0
    # loop through the set
    for x in unique_set:
        total += x
    return total
