#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry:
    """Represent the class BaseGeometry"""
    def area(self):
        """Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value is an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
