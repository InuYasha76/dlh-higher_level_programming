#!/usr/bin/python3
"""
This module is about creating an object
from a JSON file
"""


import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file". (Deserialization).

    Args:
        filename: the name of the "JSON" file to read from.

    Returns:
        The Python object representation of the JSON string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
