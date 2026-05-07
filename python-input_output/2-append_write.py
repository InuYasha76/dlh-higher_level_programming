#!/usr/bin/python3
"""This module is about Files manipulation/appending"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).
    Returns the number of characters added.
    Args:
        filename (string): name of the file to write to
        text (string, utf-8): text to append
    """
    with open(filename, 'a', encoding='utf-8') as f:
        nb_chars_written = f.write(text)
        return nb_chars_written
