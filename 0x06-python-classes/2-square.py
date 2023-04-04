#!/usr/bin/python3


class Square:
    """Represent square."""

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self._size = size
        else:
            raise TypeError('size must be an integer')
