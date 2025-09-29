#!/usr/bin/python3
"""Function that returns an object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string to deserialize.

    Returns:
        any: Python object represented by `my_str`.
    """
    return json.loads(my_str)
