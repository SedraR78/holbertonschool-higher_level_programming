#!/usr/bin/python3
""" class Square"""

class Square:
    """Represents a square.

    This class currently has no properties or methods.
    It can be extended later to include specific functionalities
    related to a square.
    """
    def __init__(self, size=0):
        self.size = size  # Using the setter

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return self.size * self.size
