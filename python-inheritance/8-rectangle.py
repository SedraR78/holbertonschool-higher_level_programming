#!/usr/bin/python3
"""
Module 8-rectangle
Defines the Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""create a subclasse Rectangle of BaseGeometry """

class Rectangle(BaseGeometry):
    """Represents a Rectangle"""

    def __init__(self, width, height):
        """ setting widht + height in private instance"""
        self.integer_validator("width", width)
        self.__width = width
        
        self.integer_validator("height", height)
        self.__height = height
