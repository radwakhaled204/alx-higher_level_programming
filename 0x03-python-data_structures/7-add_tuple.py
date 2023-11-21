#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they are smaller than 2
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    # Zip the tuples, add the corresponding elements using list comprehension
    result = [a + b for a, b in zip(tuple_a[:2], tuple_b[:2])]
    # Convert the result list to a tuple and return it
    return tuple(result)
