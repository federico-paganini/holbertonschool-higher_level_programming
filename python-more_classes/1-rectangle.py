#!/usr/bin/python3


class Rectangle:
    """
    Represents a rectangle with width and height.
    Attributes are private and validated upon assignment.
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
            TypeError: If value is not an integer (bool excluded).
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
    if type(value) != int:
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be >= 0")

    return value
