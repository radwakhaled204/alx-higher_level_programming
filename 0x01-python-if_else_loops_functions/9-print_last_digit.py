#!/usr/bin/python3
def print_last_digit(number):
    last_char = str(number)[-1]
    last_digit = int(last_char)
    print(last_digit, end="")
    return last_digit
