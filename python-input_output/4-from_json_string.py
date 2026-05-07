#!/usr/bin/python3
"""This module is about serializing Python objects to JSON"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: a string instance containing a JSON document
    """
    return json.loads(my_str)
