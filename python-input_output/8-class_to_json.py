#!/usr/bin/python3

"""return the dict w simple data struct (json serialization)"""


def class_to_json(obj):
    return obj.__dict__.copy()
