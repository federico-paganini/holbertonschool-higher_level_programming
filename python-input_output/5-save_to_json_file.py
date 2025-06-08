#!/usr/bin/python3
"""
This module provides a function to save a Python object
to a file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file in JSON format.

    Args:
        my_obj (object): The Python object to be serialized.
        filename (str): The name of the file to write the JSON string into.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
