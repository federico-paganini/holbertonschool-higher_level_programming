#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON filename. Overwrites if exists.
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): Input JSON filename.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, "r") as f:
        return json.load(f)
