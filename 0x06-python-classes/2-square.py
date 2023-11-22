#!/usr/bin/python3

"""The module that defines square """


class Square:
    """This function represents square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: size of the square defined
        Raises:
            TypeError: is not integer
            ValueError: less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
