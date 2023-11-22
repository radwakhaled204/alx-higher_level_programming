#!/usr/bin/python3

def magic_calculation(a, b):
    # Initialize a variable to store the result
    result = 0
    # Use a for loop to iterate over the range from 1 to 3
    for i in range(1, 3):
        # Use a try-except block to handle possible errors
        try:
            # If i is greater than a, raise an exception with a message
            if i > a:
                raise Exception("Too far")
            # Otherwise, update the result with a power and division operation
            else:
                result += (a ** b) / i
        # If an exception occurs, update the result with addition
        except Exception:
            result = b + a
            break
    # Return the result
    return result
