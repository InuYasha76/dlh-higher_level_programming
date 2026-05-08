#!/usr/bin/python3
"""This Module defines a CustomObject"""


import pickle


class CustomObject:
    """A class that represents a CustomObject."""

    def __init__(self, name, age, is_student):
        """
        Initializes a new CustomObject.

        Args:
            name (str): The name of the CustomObject.
            age (int): The age of the CustomObject.
            is_student (bool): A bolean flag indicating
            whether or not the instance is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the CustomObject to stdout in a customized way."""
        print(f"Name: {self.name}")
        print(f"Age {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance of the object using pickle.
        Save the serialization to the provided filename.
        Args:
            filename (string): The name of the file to write the
            serialized object to.
        Raises:
            Exception in case pickling failed for any good reason.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes the representation of a CustomObject.
        Args:
            filename: The file to read the serialized reprensation from.
        Raises:
            Exception: if the unpickling failed.
        instance of the object using pickle.
        """
        try:
            with open(filename, "rb") as f:
                pickle.load(f)
        except Exception:
            return None
