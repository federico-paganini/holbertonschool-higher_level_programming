#!/usr/bin/python3
"""
Module that defines a Student class with a method
to retrieve its dictionary representation for JSON serialization.
"""


class Student:
    """
    Represents a student with basic attributes.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
