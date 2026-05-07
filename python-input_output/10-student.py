#!/usr/bin/python3
"""This module defines at class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
                return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
            return self.__dict__
