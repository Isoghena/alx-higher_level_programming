#!/usr/bin/python3
"""Defines a the function is_same_class."""



def is_same_class(obj, a_class):
    """Return true if obj is the exact class,otherwise false."""
    return (type(obj) == a_class)
