#!/usr/bin/python3
""" 
Adding the sum of two integers.
"""


def add_integer(a, b=98):
"""Return the sum of two integers."""
    if type (a) is int or type (a) is float:
        if type (b) is int or type (b) is float:
            return int(a+b)
            else:
                raise TypeError("b must be an integer or float")
    else:
        raise TypeError("a must be an integer or float")

