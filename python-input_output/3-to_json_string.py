#!/usr/bin/python3
"""This module is about I/O and serialization"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
        my_obj (object): the object to serialize in JSON
    """
    return (json.dumps(my_obj))
