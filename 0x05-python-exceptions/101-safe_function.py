#!/usr/bin/python3

def safe_function(fct, *args):
    # a try-except block to handle possible errors
    try:
        # Call the function with the given arguments and return the result
        return fct(*args)
    except Exception as e:
        # import sys
        import sys
        # print the error message preceded by Exception: to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        # returns None if something happens during the function
        return None
