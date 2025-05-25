#!/usr/bin/python3
"""
Defines a Rectangle class with validated width and height attributes.

This module provides:
- A Rectangle class with encapsulated, validated width and height.
- Validation that ensures values are strictly integers (excluding booleans).
- Area and perimeter computation.
- Use of property decorators for controlled attribute access.
"""


class Rectangle:
    """
    Represents a rectangle defined by width and height.

    Width and height must be non-negative integers  .
    Attribute access is managed via properties with validation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""

        return "\n".join(
            [f"{self.print_symbol}" * self.__width for _ in range(self.__height)]
        )

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = validate_size(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = validate_size(value, "height")

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def area(self):
        return self.__width * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2


def validate_size(value, name):
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be >= 0")

    return value
