#!/usr/bin/python3
"""Function that returns the JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object.

    Args:
        my_obj (any): The object to serialize.

    Returns:
        str: JSON string representation of `my_obj`.
    """
    return json.dumps(my_obj)
