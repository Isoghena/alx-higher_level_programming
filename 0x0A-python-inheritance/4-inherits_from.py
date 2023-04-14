#!/usr/bin/python3
"""Defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Returns true if obj is a_class subclass,else false"""
    if issubclass(type(obj, a_class) and type(obj) != a_class:
        return True
    return False
