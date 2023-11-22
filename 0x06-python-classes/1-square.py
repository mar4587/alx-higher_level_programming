#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """This function represents 
	the square"""

    def __init__(self, size=0):
        """Initializes the new Square

        Args:
            size (int): a new square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
