#!/usr/bin/python3
"""Class Rectangle that defines a rectangle."""
class Rectangle:
    """Defines a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):               # Check type
            raise TypeError("width must be an integer")
        if value < 0:                                # Check value
            raise ValueError("width must be >= 0")
        self._width = value                          # Store valid width

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):               # Check type
            raise TypeError("height must be an integer")
        if value < 0:                                # Check value
            raise ValueError("height must be >= 0")
        self._height = value                         # Store valid height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:      # Zero width or height → no perimeter
            return 0
        return 2 * (self.width + self.height)        # Perimeter formula

    def __str__(self):
        """Return the rectangle as a string of '#' characters."""
        if self.width == 0 or self.height == 0:      # Empty rectangle
            return ""
        # Repeat '#' width times per line, for height lines
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Return an official string representation of the rectangle."""
        # This can recreate the object using eval()
        return f"Rectangle({self.width}, {self.height})"
