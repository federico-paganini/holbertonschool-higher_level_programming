#!/usr/bin/python3
"""
Module that defines a function to generate a dictionary representation
of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class with only serializable attributes
             (list, dictionary, string, integer, boolean).

    Returns:
        dict: A dictionary containing all serializable attributes of the object.
    """
    return obj.__dict__
