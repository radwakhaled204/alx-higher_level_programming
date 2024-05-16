#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # create new list to store result
    new_list = []
    # loop through the original list
    for x in my_list:
        # if element matches search replace it
        if x == search:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
