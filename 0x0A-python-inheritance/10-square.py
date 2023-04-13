#!/usr/bin/python3
"""Defines class BaseGeometry and Rectangle subclass"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Instantiation of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

        def area(self):
            """Returns the area of square"""
            return self.__size ** 2
