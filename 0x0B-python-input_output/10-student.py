#!/usr/bin/python3
"""Defining a class Student."""


class Student:
    """Representing a student."""

    def __init__(sel, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): 1st name of the student.
            last_name (str): last name of the student.
            age (int): The student's age.
        """
        sel.first_name = first_name
        sel.last_name = last_name
        sel.age = age

    def to_json(sel, attrs=None):
        """Find a dictionary rep of the Student.

        If attrs is a list of strings, rep only those attr
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {q: getattr(sel, q) for q in attrs if hasattr(sel, q)}
        return sel.__dict__
