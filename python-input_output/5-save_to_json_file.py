#!/usr/bin/python3
"""This module is about JSON serialization"""


import json


def save_to_json_file(my_obj, filename):
    """
    Method that writes an Object to a text file,
    using a JSON representation.
    Args:
        my_obj: a Python object to serialize
        filename: the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
