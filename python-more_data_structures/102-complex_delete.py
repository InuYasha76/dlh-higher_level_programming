#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        for k in list(a_dictionary.keys()):
            if a_dictionary.get(k) == value:
                a_dictionary.pop(k, None)
    return a_dictionary
