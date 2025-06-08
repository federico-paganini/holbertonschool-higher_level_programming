#!/usr/bin/python3
"""
This module provides a function to deserialize a JSON-formatted string
into its corresponding Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string into a Python object.

    Args:
        my_str (str): A string containing a valid JSON structure.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
