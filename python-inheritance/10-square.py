#!/usr/bin/python3
"""
Defines the Square class that inherits from Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

"""create a subclasse Square of BaseGeometry """

class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """ setting  size in private instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__size}/{self.__size}"
