#!/usr/bin/python3

def roman_to_int(roman_string):
    # check if the roman_string is a string or None
    if not isinstance(roman_string, str):
        # return 0
        return 0
    # create a dictionary to store the values of the roman numerals
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # create a variable to store the result
    result = 0
    # loop through each character in the roman_string from left to right
    for i in range(len(roman_string)):
        # get the value of the current character
        current = values[roman_string[i]]
        if i < len(roman_string) - 1 and values[roman_string[i + 1]] > current:
            # subtract the current value from the result
            result -= current
        else:
            result += current
    return result
