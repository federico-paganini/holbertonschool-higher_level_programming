#!/usr/bin/python3
"""
This module provides a function `append_after` that allows you to insert
a specific line of text (`new_string`)
immediately **after** every line in a file
that contains a specific `search_string`.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text (new_string) after each line that contains a given search_string.

    Args:
        filename (str): Name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each matching line.
    """
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
