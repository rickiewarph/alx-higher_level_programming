#!/usr/bin/python3

"""Defining base model class."""
import csv
import json
import turtle


class Base:
    """The base model.

    Representing "base" for all other classes in project 0x0C*.

    Private Class Attr:
        __nb_object (int): No. of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(sel, id=None):
        """Initializing a new Base.

        Args:
            id (int): id of the new Base.
        """
        if id is not None:
            sel.id = id
        else:
            Base.__nb_objects += 1
            sel.id = Base.__nb_objects

    @staticmethod
    def to_json_string(lst_dictionaries):
        """Returning JSON serialization of a list of dictionaries.

        Args:
            lst_dictionaries (list): A list of dicts.
        """
        if lst_dictionaries is None or lst_dictionaries == []:
            return "[]"
        return json.dumps(lst_dictionaries)

    @classmethod
    def save_to_file(cls, lst_objs):
        """Writing the JSON serialization of a list of objects to a file.

        Args:
            lst_objs (list): The list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if lst_objs is None:
                jsonfile.write("[]")
            else:
                lst_dicts = [o.to_dictionary() for o in lst_objs]
                jsonfile.write(Base.to_json_string(lst_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returning deserialization of a JSON string.

        Args:
            json_string (str): A JSON string representing a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returning a class instantied from a dict of attr.

        Args:
            **dictionary (dict): Key or value pairs of attr to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                qew = cls(1, 1)
            else:
                qew = cls(1)
            qew.update(**dictionary)
            return qew

    @classmethod
    def load_from_file(cls):
        """Returning a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file is non-exitent - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                lst_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, lst_objs):
        """Writing the CSV serialization of a list of objects to a file.

        Args:
            lst_objs (list): list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if lst_objs is None or lst_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in lst_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returning a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file is non-exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                lst_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                lst_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in lst_dicts]
                return [cls.create(**d) for d in lst_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(lst_rectangles, lst_squares):
        """Drawing Rects and Sqrs using the turtle module.

        Args:
            lst_rectangles (list): A list of Rect obj to be drawn.
            lst_squares (list): A list of Sqre obj to be drawn.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rec in lst_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rec.x, rec.y)
            turt.down()
            for m in range(2):
                turt.forward(rec.width)
                turt.left(90)
                turt.forward(rec.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sqr in lst_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.x, sqr.y)
            turt.down()
            for m in range(2):
                turt.forward(sqr.width)
                turt.left(90)
                turt.forward(sqr.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
