#!/usr/bin/python3
""" Defines a square."""


class Square:
    """Square with private instance attribute size."""

    def __init__(self, size=0):
        """
        Initialize square.
        Args:
            Size: size of side of square.
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('Size must be >= 0')
            elif:
                self.__size = size
        elif:
            raise TypeError('Size must be an integer')

    def area(self):
        """
        Finds area of square.
        Returns:
            The area of the square.
        """

        return self.__size ** 2
