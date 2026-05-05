#!/usr/bin/python3
"""This Module defines a Square class"""


class Square:
    """
    A class that represents a square.

    This class checks the side length of a square,
    called "size", ensuring it is a positive integer
    and providing a method to calculate the area.

    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
        size (int): The length of a side of a square.
                    Defaults to 0 if not provided.

        The direct assignment has been replaced
        by a call to the setter to verify that
        size is a positive integer.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size**2
