#!/usr/bin/python3
"""
Module 8-rectangle
Defines the Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):

        # validate width
        self.integer_validator("width", width)
        self.__width = width
        # validate height
        self.integer_validator("height", height)
        self.__height = height
