#!/usr/bin/python3
"""Defines a base model class."""


import json
import csv
import turtle


class Base:
    """A base class for other classes in the project"""

    # a private class attribute to keep track of number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional id"""

        # If id is given, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # otherwise increment the class attribute and assign it to the id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        # If list_dictionaries is None or empty, return the string "[]"
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        # Otherwise, use the json.dumps method to return
        # the JSON string representation of list_dictionaries
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        list_dicts = [obj.to_dictionary() for obj in list_objs] \
            if list_objs else []

        # Use the to_json_string method to get
        # the JSON string representation of list_dicts
        json_string = cls.to_json_string(list_dicts)

        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        # If json_string is None or empty, return an empty list
        if json_string is None or not json_string:
            return []

        # Otherwise, use the json.loads method to
        # return the list represented by json_string
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                data = f.read()
                list_dict = cls.from_json_string(data)
                list_inst = []
                for d in list_dict:
                    list_inst.append(cls.create(**d))
                return list_inst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                list_dict = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        list_dict.append({"id": int(row[0]),
                                          "width": int(row[1]),
                                          "height": int(row[2]),
                                          "x": int(row[3]),
                                          "y": int(row[4])})
                    elif cls.__name__ == "Square":
                        list_dict.append({"id": int(row[0]),
                                          "size": int(row[1]),
                                          "x": int(row[2]),
                                          "y": int(row[3])})
                list_inst = []
                for d in list_dict:
                    list_inst.append(cls.create(**d))
                return list_inst
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the Rectangles and Squares using Turtle graphics"""

        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        for r in list_rectangles:
            t.penup()
            t.goto(r.x, r.y)
            t.pendown()
            t.color("red")
            t.begin_fill()
            for i in range(2):
                t.forward(r.width)
                t.left(90)
                t.forward(r.height)
                t.left(90)
            t.end_fill()
        for s in list_squares:
            t.penup()
            t.goto(s.x, s.y)
            t.pendown()
            t.color("blue")
            t.begin_fill()
            for i in range(4):
                t.forward(s.size)
                t.left(90)
            t.end_fill()
        turtle.done()
