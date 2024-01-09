#!/usr/bin/python3
"""To define a string-to-JSON func."""
import json


def to_json_string(my_objt):
    """Returning JSON representative of a string object."""
    return json.dumps(my_objt)
