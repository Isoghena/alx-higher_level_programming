#!/usr/bin/python3
"""Function that a string."""


def say_my_name(first_name, last_name=""):
    """Prints out "My name is" followed by first name and last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
