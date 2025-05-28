#!/usr/bin/python3
"""
This module defines a custom class MyList that inherits
from the built-in list.
It adds a method to print the list elements in ascending sorted order.
"""


class MyClass(list):
    """
    MyList is a subclass of the built-in list.
    It includes an additional method to print the list sorted in ascending order,
    without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        This method does not modify the original list. It uses the built-in
        sorted() function to display a sorted version of the list.
        """
        print(sorted(self))
