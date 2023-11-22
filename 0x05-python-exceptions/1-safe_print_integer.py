#!/usr/bin/python3

def safe_print_integer(value):
    # a try-except block to hanlde any possible error
    try:
        # print value of integer
        print("{:d}".format(value))
        return True
    # catch any ValueError or TypeError may occur
    except (ValueError, TypeError):
        return False
