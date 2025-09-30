#!/usr/bin/python3
"""creating an Obj from a JSON file"""

import json


def load_from_json_file(filename):
    """Deserialize a JSON file into a Python object."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
     
    