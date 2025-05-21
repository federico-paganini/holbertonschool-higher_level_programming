#!/usr/bin/python3
"""
max_integer module.

This module provides a function to find the maximum integer
in a list of integers or floats.
"""


def max_integer(list=[]):
    """Finds and returns the maximum integer in a list.

    Args:
        list (list): A list of integers or floats.

    Returns:
        The maximum number in the list, or None if the list is empty.
    """

    if not list:
        return None

    max_value = list[0]
    for num in list[1:]:
        if num > max_value:
            max_value = num

    return max_value
