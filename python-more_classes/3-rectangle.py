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

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Must be an integer >= 0.
            height (int): The height of the rectangle. Must be an integer >= 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        self.__width = validate_size(value, "width")

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): The new height to set.

        Raises:
            TypeError: If value is not an integer (bool excluded).
            ValueError: If value is less than 0.
        """
        self.__height = validate_size(value, "height")

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
        str: A string with lines of '#' forming the rectangle, or
             an empty string if width or height is 0.
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter, or 0 if either side is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area.
        """
        return self.__width * self.__height


def validate_size(value, name):
    """
    Validate that the value is strictly an int.

    Args:
        value: The value to validate.
        name (str): The name of the attribute, used in error messages.

    Returns:
        int: The validated value.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be >= 0")

    return value
