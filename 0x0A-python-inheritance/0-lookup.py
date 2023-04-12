#!/usr/bin/python3
"""Defines object attribute lookup function."""


def lookup(obj):
    """Returns a list of available attributes and methods of object."""
    return dir(obj)


