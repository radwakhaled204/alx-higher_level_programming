#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


# Import BaseGeometry from 7-base_geometry module
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle with width and height"""
        # Validate width and height as positive integers
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Assign width and height as private attributes
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
