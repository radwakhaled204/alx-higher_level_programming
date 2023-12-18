#!/usr/bin/python3
""" a class MyInt that inherits from int"""


class MyInt(int):
    """A class that inherits from int and has inverted operators"""

    def __eq__(self, other):
        """Returns True if self and other are not equal, False otherwise"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns True if self and other are equal, False otherwise"""
        return super().__eq__(other)
