#!/usr/bin/python3
""" class Square"""

class Square:
    """Represents a square.

    This class currently has no properties or methods.
    It can be extended later to include specific functionalities
    related to a square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
