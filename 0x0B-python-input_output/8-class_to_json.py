#!/usr/bin/python3
"""Defining a Python class-to-JSON func."""


def class_to_json(objt):
    """Returing the dictionary represntative of a simple data struct."""
    return objt.__dict__
