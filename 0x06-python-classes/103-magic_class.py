#!/usr/bin/python3
"""This function defines a class MagicClass"""
import math


class MagicClass:
    """represents the circle"""

    def __init__(self, radius=0):
        """This initializes the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculaes the area of the circle"""

        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius
