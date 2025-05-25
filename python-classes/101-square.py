#!/usr/bin/python3
"""
Module that defines a Square class with size and position.

This module provides a Square class capable of calculating its area
and printing a visual representation of itself considering its position.
"""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        if self.__size == 0:
            return ""

        square_lines = [
            " " * self.__position[0] + "#" * self.__size
            for _ in range(self.__size)
        ]
        return "\n" * self.__position[1] + "\n".join(square_lines)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        print(self)
