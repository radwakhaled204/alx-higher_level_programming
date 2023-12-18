Usage:

To use the classes, you can import them from the models package:

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

To run the unittests, you can use the following command:

python3 -m unittest discover tests

To create an instance of a class, you can use the constructor with the appropriate arguments:

r1 = Rectangle(10, 2)
s1 = Square(5)

To access or modify the attributes of an instance, you can use getters and setters or dot notation:

r1.width # getter
r1.width = 12 # setter
r1.x # dot notation
r1.x = 3 # dot notation

