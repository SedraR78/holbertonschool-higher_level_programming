#!/usr/bin/python3
""" class Square"""

class Square:
    """Represents a square.

    This class currently has no properties or methods.
    It can be extended later to include specific functionalities
    related to a square.
    """
    def __init__(self,size):
        self.__size = size

    def get_size(self):
        return self
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
