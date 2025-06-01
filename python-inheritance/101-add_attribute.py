#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object.
"""


def add_attr(obj, attr, value):
    """
    Adds a new attribute to an object if it doesn't already exist.

    Args:
        obj: The object to which the attribute will be added.
        attr (str): The name of the attribute.
        value: The value to set for the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, attr):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
