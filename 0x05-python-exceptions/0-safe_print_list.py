#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # initialize a variable to to count number of elements printed
    count = 0
    # loop through the range of x
    for i in range(x):
        # try to print the element at index i of the list
        try:
            print(my_list[i], end="")
            count += 1
        # break the loop if index is out of range
        except IndexError:
            break
        # print a new line after the loop
    print()
    return count
