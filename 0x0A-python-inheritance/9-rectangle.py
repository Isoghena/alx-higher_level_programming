#!/usr/bin/python3
"""Defines a class Rectangle that inherits BaseGeometry"""


class BaseGeometry:
    """A class with public instance"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer". format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Instantiation of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
