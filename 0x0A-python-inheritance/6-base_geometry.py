#!/usr/bin/python3
"""This module defines a class BaseGeometry with a public instance area"""


class BaseGeometry:
    """A base class for geometry objects"""

    def area(self):
        """Raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
