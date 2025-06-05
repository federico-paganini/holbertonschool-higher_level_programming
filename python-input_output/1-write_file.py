#!/usr/bin/python3
"""
This module provides a function to write text to a UTF-8 encoded file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file
    and returns the number of characters written.

    If the file already exists, it will be overwritten.
    If it does not exist, it will be created.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write into the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
