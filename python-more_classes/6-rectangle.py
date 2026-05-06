#!/usr/bin/python3
"""
This module defines an empty class Rectangle.
"""


class Rectangle:
    """An empty class that defines a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width: int, optional, O if not provided
            height: int, optional, 0 if not provided
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates the area of a Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of a Rectangle.
        If width or height equal to 0, perimeter = 0.
        """
        return (
            0
            if not (self.__width and self.__height)
            else 2 * (self.__width + self.__height)
        )

    def __str__(self):
        """Returns the Rectangle with the character #."""
        return (
            ""
            if not (self.__width and self.__height)
            else "\n".join(["#" * self.__width for _ in range(self.__height)])
        )

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        allowing to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
