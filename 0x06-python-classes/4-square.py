#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class represents a square with private instance attribute: size"""

    def __init__(self, size=0):
        """Initializes the square with the given size"""
        self.size = size  # Note the use of the setter

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
