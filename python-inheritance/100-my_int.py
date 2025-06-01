#!/usr/bin/python3
"""
This module defines the MyInt class which inherits from int
but inverts the behavior of == and != operators.
"""


class MyInt(int):
    """
    MyInt is a subclass of int that inverts the behavior of
    the equality (==) and inequality (!=) operators.
    """

    def __eq__(self):
        return super().__ne__(other)

    def __ne__(self):
        return super().__eq__(other)
