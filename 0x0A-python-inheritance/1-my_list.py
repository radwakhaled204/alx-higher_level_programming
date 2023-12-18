#!/usr/bin/python3
"""This a module of subclass of list that can print itself sorted"""


class MyList(list):
    """A subclass of list that can print itself sorted"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
