#!/usr/bin/python3
"""This modules is about files manipulation"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string.
    """
    with open(filename, "r", encoding="utf-8") as fr:
        lines = fr.readlines()
    new_text = []
    for line in lines:
        new_text.append(line)
        if search_string in line:
            new_text.append(new_string)
    with open(filename, "w", encoding="utf-8") as fw:
        fw.writelines(new_text)
