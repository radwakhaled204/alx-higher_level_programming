#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Class that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        # Use the built-in __dict__ attribute to get
        # the dictionary of the object's attributes
        return self.__dict__
