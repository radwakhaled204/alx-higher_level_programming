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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list of str, optional): The list of
            attribute names to retrieve. Defaults to None.
        """
        # If attrs is a list of strings, only attribute
        # names contained in this list must be retrieved.
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            result = {attr: getattr(self, attr) for attr in attrs
                      if hasattr(self, attr)}
            return result

        # Otherwise, all attributes must be retrieved
        else:
            # Use the built-in __dict__ attribute to
            # get the dictionary of the object's attributes
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): The dictionary of new attribute values
        """
        # Iterate over the keys and values of the json dictionary
        for key, value in json.items():
            # Use the built-in setattr function
            # to set the new value to the attribute
            setattr(self, key, value)
