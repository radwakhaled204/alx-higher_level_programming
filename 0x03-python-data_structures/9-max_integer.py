#!/usr/bin/python3

def max_integer(my_list=[]):
    # check if the list is empty and return none if emtpy
    if not my_list:
        return None
    else:
        # initialize the max value as a first element of the list
        max_value = my_list[0]
        # loop through the rest of the list
        for x in my_list:
            # compare between
            if x > max_value:
                max_value = x
        return max_value
