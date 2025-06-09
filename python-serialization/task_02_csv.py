#!/usr/bin/python3
"""
This module defines a function to convert data from a CSV file into JSON format.
It uses the csv module to read the file and the json module to write the output.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file into a JSON file named 'data.json'.

    Each row in the CSV file is converted into a dictionary using csv.DictReader,
    and the resulting list of dictionaries is written to a JSON file.

    Args:
        csv_filename (str): The path to the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False

    except Exception as e:
        print(f"Error during conversion: {e}")
        return False
