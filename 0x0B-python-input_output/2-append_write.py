#!/usr/bin/python3
"""Function appends a string"""


def append_write(filename="", text=""):
    """Return the numbers of charaters added"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
