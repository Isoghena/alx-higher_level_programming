#!/usr/bin/python3
"""Contains an inherited list class Mylist."""


class Mylist(self):
    """Subclass of list."""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints sorted list."""
        print(sorted(self))
