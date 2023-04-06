#!/usr/bin/python3
"""
Define a class Rectangle.
"""


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize  rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter private instance attribute of width"""
        return self.__width

    @width.setter
    def width(self,value):
        """setter private intance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
        
    @property
    def height(self):
        """getter private instance attribute of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter private instance attribute of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
