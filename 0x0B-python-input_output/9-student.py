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

    def to_json(sel):
        """Locate a dictionary representation of the Student."""
        return sel.__dict__
