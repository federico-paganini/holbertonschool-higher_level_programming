#!/usr/bin/python3
"""
This module provides functionality to serialize a Python dictionary to an XML file
and to deserialize an XML file back into a Python dictionary.

Functions:
    - serialize_to_xml(dictionary, filename)
    - deserialize_from_xml(filename)
"""

import xml.etree.ElementTree as ET


import xml.etree.ElementTree as ET
from xml.dom import minidom


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The filename to save the XML data
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child_element = ET.SubElement(root, key)
        child_element.text = str(value)

    tree = ET.ElementTree(root)

    xml_str = ET.tostring(root, encoding="unicode")
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="    ")

    lines = pretty_xml.split("\n")[1:]
    lines = [line for line in lines if line.strip()]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def deserialize_from_xml(filename):
    """
    Deserialize XML data from file back to a Python dictionary.

    Args:
        filename (str): The filename to read XML data from

    Returns:
        dict: The deserialized dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}

    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
