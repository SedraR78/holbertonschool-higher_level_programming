#!/usr/bin/python3
""" mary j is in the spot tonight"""
def inherits_from(obj, a_class):
    """Retourne True si obj est instance d’une sous-classe de a_class (mais pas a_class lui-même)"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class