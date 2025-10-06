#!/usr/bin/env python3
"""
CSV to JSON Converter
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and writes to data.json
    
    Args:
        csv_filename (str): The name of the CSV file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV data and convert to list of dictionaries
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        # Serialize and write JSON data
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False