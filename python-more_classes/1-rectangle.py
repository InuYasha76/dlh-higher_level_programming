#!/usr/bin/python3
"""
This module defines an empty class Rectangle.
"""


class Rectangle:
    """An empty class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width: int, optional, O if not provided
            height: int, optional, 0 if not provided
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets:
            The width of a Rectangle.
        Args:
            value: int.
        Raises:
            TypeError: if not integer.
            ValueError: if not positive.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets:
            The height of a Rectangle.
        Args:
            value: int.
        Raises:
            TypeError: if not integer.
            ValueError: if not positive.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
