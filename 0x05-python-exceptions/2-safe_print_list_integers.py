#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # intialize a variable to count number of printed elements
    count = 0
    # loop to iterate over the first x elements of the list
    for i in range(x):
        # a try-except block to handle possible errors
        try:
            # print the element as an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1
        # catch any ValueError or TypeError may occur
        except (ValueError, TypeError):
            # skip the element if not integer
            pass
    # print new line after loop
    print()
    # return the number of printed integer
    return count
