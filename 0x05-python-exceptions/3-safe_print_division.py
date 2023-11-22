#!/usr/bin/python3

def safe_print_division(a, b):
    # initialize a variable to store result of the division
    result = None
    # try-except-finally block to handle possible errors
    try:
        result = a / b
    except ZeroDivisionError:
        # Handle the case when b is zero
        pass
    finally:
        # print the result in finally section
        print("Inside result: {}".format(result))
        # return the result or None
        return result
