#!/usr/bin/python3
"""Defines a square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance with the given attributes"""

        # Call the super class
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance"""

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """The getter for the size attribute"""

        return self.width

    @size.setter
    def size(self, value):
        """The setter for the size attribute"""

        # Assign the value to both the width and height attributes
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument or a key/value argument to attributes"""

        # Use a list of attribute names to map the arguments
        attributes = ["id", "size", "x", "y"]

        # Iterate over the arguments and assign them to the attributes
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

        # If no arguments are given, iterate over the keyword
        # arguments and assign them to the attributes
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        # Use a dictionary literal to create and return the dictionary
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
