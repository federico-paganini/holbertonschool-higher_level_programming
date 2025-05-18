#!/usr/bin/python3
"""
This module provides a function to add two integers or floats,
casting them to integers first.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int or float): First number
        b (int or float): Second number, defaults to 98

    Returns:
        int: The result of adding a and b after casting to int

    Raises:
        TypeError: If a or b are not integers or floats

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100)
    198
    >>> add_integer(1.5, 2.7)
    3
    >>> add_integer("3", 4)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
