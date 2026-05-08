#!/usr/bin/python3
"""This module is about de/serializing XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to the given filename.
    
    Args:
        dictionary (dict): The dictionary to serialize to XML.
        filename (str): The name of the file to serialize to.
    
    Returns:
        None
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
    for key, value in dictionary.items():
        xml_child_node = ET.SubElement(xml_root, key)
        xml_child_node.text = str(value)
        # sets the type of the node for deterministic type deserialization
        xml_child_node.set("type", type(value).__name__)
    # Apply human readable formatting
    ET.indent(xml_root, space="    ", level=0)
    # Uses the ET.ElementTree class to handle high-level operations (write)
    xml_dom_tree = ET.ElementTree(xml_root)
    xml_dom_tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Read the XML data from that file, returns a deserialized Python dictionary.
    Implements type conversion.
    Args:
        filename (str): the name of the xml file to convert to Python object
    Returns:
        dict: A dictionary, None if errors
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        reconstruct_dict = {}
        for child in root:
            text_value = child.text if child.text is not None else ""
            value_type = child.get("type", "str")
            if value_type == "int":
                value = int(text_value)
            elif value_type == "float":
                value = float(text_value)
            elif value_type == "bool":
                value = True if text_value.lower() == "true" else False
            else:
                value = text_value
            reconstruct_dict[child.tag] = value
        return reconstruct_dict
    except Exception:
        return None
