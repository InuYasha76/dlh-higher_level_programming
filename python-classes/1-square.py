#!/usr/bin/python3
"""This Module defines a Square class"""


class Square:
    """
    A class that represents a square.

    Attributes:
        size (int): The length of a side of a square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
        size (int): The size of the new square.
        """
        self.__size = size
