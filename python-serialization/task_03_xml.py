#!/usr/bin/env python3
"""
XML Serialization and Deserialization
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file.
    
    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the file to save the XML to
        
    Returns:
        None
    """
    try:
        # Create the root element
        root = ET.Element("data")
        
        # Iterate through dictionary items and add them as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convert all values to strings for XML
        
        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        
        # Write with pretty formatting (indentation)
        with open(filename, 'wb') as file:
            # Add XML declaration and pretty print
            file.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            tree.write(file, encoding='utf-8')
            
    except Exception as e:
        print(f"Error during serialization: {e}")


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file and returns a Python dictionary.
    
    Args:
        filename (str): The name of the XML file to read from
        
    Returns:
        dict: The deserialized dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from XML elements
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
        
        return result_dict
        
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return {}
