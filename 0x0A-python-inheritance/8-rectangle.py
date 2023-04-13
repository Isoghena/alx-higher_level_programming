#!/usr/bin/python3
"""Defines a class Rectangle that inherits BaseGeometry"""


class Rectangle(BaseGeometry):
    """Represent a rectangle."""
    def __init__(self, width, height):
        """Instantiation of rectangle."""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
