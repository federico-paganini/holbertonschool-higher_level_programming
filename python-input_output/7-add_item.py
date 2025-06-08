#!/usr/bin/python3
"""
This module handles adding command-line arguments to a JSON file.

If the file doesn't exist, it creates one. If it exists, it loads
its content (a list), appends the new items passed as command-line
arguments, and saves the updated list back to the file.

Modules used:
- sys: for accessing command-line arguments.
- json: via custom save/load helper functions.

Functions imported:
- save_to_json_file: saves a Python object as JSON to a file.
- load_from_json_file: loads a Python object from a JSON file.
"""

import sys

save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file
av = sys.argv[1:]

try:
    data = load_json("add_item.json")
except FileNotFoundError:
    data = []

data.extend(av)
save_json("add_item.json", data)
