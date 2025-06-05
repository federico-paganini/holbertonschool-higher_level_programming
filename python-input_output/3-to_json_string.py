#!/usr/bin/python3
"""
This module provides a function to convert a Python object
to its JSON string representation.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: The JSON-formatted string representation of the object.
    """
    return json.dumps(my_obj)
