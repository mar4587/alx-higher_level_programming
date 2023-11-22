#!/usr/bin/python3

"""This defines class Square"""


class Square:
    """represents a square
    Attributes:
        __size (int): side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """This calculates the square area
        Returns:
            area of square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """it is the getter of __size
        Returns:
            size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):

        """the setter of __size
        Args:
            value (int): a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """This prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()

            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
