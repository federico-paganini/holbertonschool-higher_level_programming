#!/usr/bin/python3
"""
This module defines a custom Python class named CustomObject and demonstrates
how to serialize and deserialize instances of this class
using the pickle module.

Features:
- CustomObject class with attributes: name, age, is_student
- Instance method to display the object's data
- Serialization and deserialization methods using pickle
- Exception handling for file I/O and pickle errors
"""
import pickle
import os


class CustomObject:
    """
    A custom Python object with basic attributes and methods to
    serialize and deserialize itself using the pickle module.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (pickle.PickleError, IOError) as err:
            print(f"Serialization failed: {err}")

    @classmethod
    def deserialize(cls, filename):
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return None

        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject.")
                    return None
        except (pickle.PickleError, IOError, EOFError) as error:
            print(f"Deserialization failed: {error}")
            return None
