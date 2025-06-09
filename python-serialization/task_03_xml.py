#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize Python dictionaries
using XML as an alternative to JSON.

Functions:
- serialize_to_xml(dictionary, filename)
- deserialize_from_xml(filename)
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to write the XML to.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            item = ET.SubElement(root, key)
            item.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True

    except Exception as e:
        print(f"Serialization error: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML content from a file into a dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict or None: The reconstructed dictionary, or None if there was an error.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            text = child.text
            if text is None:
                result[child.tag] = None
            elif text.lower() in ("true", "false"):
                result[child.tag] = text.lower() == "true"
            else:
                try:
                    result[child.tag] = int(text)
                except ValueError:
                    try:
                        result[child.tag] = float(text)
                    except ValueError:
                        result[child.tag] = text
        return result

    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Deserialization error: {e}")
        return None
