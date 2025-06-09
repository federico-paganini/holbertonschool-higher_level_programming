#!/usr/bin/python3
"""
This module provides functionality to serialize a Python dictionary to an XML file
and to deserialize an XML file back into a Python dictionary.

Functions:
    - serialize_to_xml(dictionary, filename)
    - deserialize_from_xml(filename)
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to write the XML to.

    Returns:
        None
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML stores text, so convert everything to str

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        pass  # silently ignore file writing errors (optional)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict or None: The deserialized dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            value = child.text

            # Optional: Try to recover data types (int, float, bool)
            if value == "True":
                result[child.tag] = True
            elif value == "False":
                result[child.tag] = False
            else:
                try:
                    result[child.tag] = int(value)
                except (ValueError, TypeError):
                    try:
                        result[child.tag] = float(value)
                    except (ValueError, TypeError):
                        result[child.tag] = value  # keep as string

        return result
    except Exception:
        return None
