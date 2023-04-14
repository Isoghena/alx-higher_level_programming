#!/bin/usr/python3
"""Define a Rectangle class Square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Represents new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
