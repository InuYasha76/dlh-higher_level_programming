#!/usr/bin/python3
"""This Module defines a Square class"""


class Square:
    """
    A class that represents a square.

    This class checks the side length of a square,
    called "size", ensuring it is a positive integer
    and providing a method to calculate the area.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
        size (int): The length of a side of a square.
                    Defaults to 0 if not provided.
        position (tuple): The position of the square.
                          Defaults to (0,)) if not provided.

        The direct assignment has been replaced
        by a call to the setter to verify that
        size is a positive integer.
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """
        Prints a square to stdout.

        The square is made of __size x __size '#' characters
        If __size is 0, or if the vertical position is > 0,
        only an empty line is printed. Else, prints as many
        space characters as the horizontal positions requires
        and then prints the square pattern made of '#'.
        """
        if not self.__size:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        Gets the position  of the square.

        Returns the position of the square as a tuple
        of two positive integers (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
