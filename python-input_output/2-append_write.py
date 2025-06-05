#!/usr/bin/python3
"""
This module provides a function to append text to a UTF-8 encoded file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 encoded text file
    and returns the number of characters added.

    If the file does not exist, it will be created.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text content to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
