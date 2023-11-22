#!/usr/bin/python3
"""This defines class Square"""


class Square:
    """This represents the square
    Attributes:
        __size (int): the size of a side of the square
    """
    def __init__(self, size=0):
        """ Initializes a square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """ This calculates the square area
        Returns:
            area of square
        """

        return (self.__size) ** 2
