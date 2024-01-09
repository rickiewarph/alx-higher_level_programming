#!/usr/bin/python3
"""Defineing a class Student."""


class Student:
    """Reping a student."""

    def __init__(sel, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): The 1st name of the student.
            last_name (str): The last name of the student.
            age (int): The student's age.
        """
        sel.first_name = first_name
        sel.last_name = last_name
        sel.age = age

    def to_json(sel, attrs=None):
        """Getting a dict representation of the Student.

        If attrs is a list of strings, reps only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {q: getattr(sel, q) for q in attrs if hasattr(sel, q)}
        return sel.__dict__

    def reload_from_json(sel, json):
        """Replacing all attr of the Student.

        Args:
            json (dict): The key pairs to replace attributes with.
        """
        for q, v in json.items():
            setattr(sel, q, v)
