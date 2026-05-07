#!/usr/bin/python3
"""This modules is about writing to a file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Returns the number of characters written
    Args:
        filename (string): the file to write to
        text (string): the text to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        chars_written = f.write(text)
        return chars_written
