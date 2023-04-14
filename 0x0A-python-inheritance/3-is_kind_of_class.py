#!/usr/bin/python3
"""Defines is-kind_of_function."""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance or inherited,otherwise false"""
    return (isinstance(obj, a_class))
