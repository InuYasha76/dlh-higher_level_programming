#!/usr/bin/python3
"""This module is about de/serializing XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes the dictionary into XML and saves it to the given filename.
    Args:
        dictionary (dict): The dictionary to serialize to XML.
        filename (string): The name of the *.xml file to serialize to.
    Returns:
        The xml representation of the serialized dictionary.
    """
    root_element = "data"
    # Creates a class ET.Element standalone root element named "data"
    xml_root = ET.Element(root_element)
    # Iterate through the dictionary items and
    # adds them as child elements to the root using ET.SubElement factory
    # ET.SubElement does two things at once:
    # - It creates a new element then
    # - Attaches it to a node that becomes its parent
    # Each newly created node is empty, text(txt) apends txt to the node
    for key, value in dictionary:
        xml_child_node = ET.SubElement(xml_root, key)
        xml_child_node.text = str(value)
    # Uses the ET.ElementTree class to handle high-level operations (write)
    xml_dom_tree = ET.ElementTree(xml_root)
    xml_dom_tree.write("data")


def deserialize_from_xml(filename):
    """
    Read the XML data from that file, returns a deserialized Python dictionary.
    Args:
        filename (string): the xml file to convert to Python object
    Returns:
        A Python dictionary, None if errors
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        reconstruct_dict = {}
        for child in root:
            value = int(child.text) if child.text.isdigit() else child.text
            reconstruct_dict[child.tag] = value
        return reconstruct_dict
    except Exceptions:
        return None
