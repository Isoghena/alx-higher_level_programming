#!/usr/bin/python3
"""Define a read-file function"""


def read_file(filename=""):
    """Read the text file(UTF8) and print it into stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
