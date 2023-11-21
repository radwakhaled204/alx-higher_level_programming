#!/usr/bin/python3
"""
This module defines a class Square with a private instance
attribute size and the corresponding property and setter methods
"""


class Square:
    """
    This class represents a square with a private instance attribute
    size and the corresponding property and setter methods"""

    def __init__(self, size=0):
        """This method initializes the square with the given size"""
        self.size = size

    @property
    def size(self):
        """This method returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This method prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
