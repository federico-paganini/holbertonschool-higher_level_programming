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

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(
            type(attr) is str for attr in attrs
        ):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])
