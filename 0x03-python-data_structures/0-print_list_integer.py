#!/usr/bin/python3

def print_list_integer(my_list=[]):
    # loop through the list
    for i in my_list:
        # print each integer using str.format()
        print("{:d}".format(i))
