#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a UTF-8 text file.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The path to the text file. Defaults to an empty string.
    """
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read(), end="")
