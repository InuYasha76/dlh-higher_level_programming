#!/usr/bin/python3
"""This module is about Python and JSON"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        The dictionary representation of the object's attributes.
    """
    return obj.__dict__
