#!/usr/bin/python3
"""Defines a rectangle class."""


from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance with the given attributes"""

        # call the super class with id
        super().__init__(id)

        # assign each argument to the right attribute
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter for the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """The setter for the width attribute"""

        # Validate the value as an integer greater than zero
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        # Assign the value to the private attribute
        self.__width = value

    @property
    def height(self):
        """The getter for the height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """The setter for the height attribute"""

        # Validate the value as an integer greater than zero
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        # Assign the value to the private attribute
        self.__height = value

    @property
    def x(self):
        """The getter for the x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """The setter for the x attribute"""

        # Validate the value as an integer greater than or equal to zero
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        # Assign the value to the private attribute
        self.__x = value

    @property
    def y(self):
        """The getter for the y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """The setter for the y attribute"""

        # Validate the value as an integer greater than or equal to zero
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        # Assign the value to the private attribute
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""

        # The area of a rectangle is width times height
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""

        for i in range(self.y):
            print()
        # use a nested loop to print the rows and columns of #
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """Returns a string representation of the Rectangle instance"""

        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        # Use a list of attribute names to map the arguments
        attributes = ["id", "width", "height", "x", "y"]

        # Iterate over the arguments and assign them to the attributes
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

        # If no arguments are given, iterate over the keyword
        # arguments and assign them to the attributes
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        # Use a dictionary literal to create and return the dictionary
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
        }
