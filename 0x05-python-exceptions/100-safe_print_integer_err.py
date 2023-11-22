#!/usr/bin/python3

def safe_print_integer_err(value):
    # try-except block to handle possible errors
    try:
        # print the value as an integer
        print("{:d}".format(value))
        # Return True if the print statement succeeds
        return True
    except Exception as e:
        # Import sys module to print to stderr
        import sys
        # Print the error message preceded by Exception: to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        # Return False if the print statement fails
        return False
