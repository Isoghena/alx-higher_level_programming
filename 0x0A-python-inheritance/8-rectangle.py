#!/usr/bin/python3
"""Defines a class Rectangle that inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle."""
    def __init__(self, width, height):
        """instantiation of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
