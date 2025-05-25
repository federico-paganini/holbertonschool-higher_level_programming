#!/usr/bin/python3
"""
This module defines a class Square that represents a square shape.

The Square class allows setting and retrieving the size of the square,
with validation to ensure that the size is always a non-negative integer.
It also provides a method to calculate the area of the square.
"""


class Square:
    """
    Represents a square with a specific size.

    This class provides methods to set and get the size of the square,
    while ensuring that it is always a non-negative integer.
    It also includes a method to calculate the area.
    """

    def __init__(self, size=0):
        self.size = size

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
