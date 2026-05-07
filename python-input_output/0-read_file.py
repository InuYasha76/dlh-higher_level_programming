#!/usr/bin/python3
"""This modules is about files manipulation"""

def read_file(filename=""):
    """
    Reads a file and prints to stdout
    Args:
        filename (string): name of the file
    """
    with open(filename, encoding="utf-8") as f:
        o = f.read()
        print(o, end='')
