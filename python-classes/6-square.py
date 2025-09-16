#!/usr/bin/python3
"""Class Square"""

class Square:
    """Represents a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square on a grid (x, y).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with a given size and its position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The coordinates of the top-left corner. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for the position attribute.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the position is not a tuple of two integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 integers")
        self._position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """Prints the square to stdout with the character #.

        If the size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print("")
        else:
            # Print position spaces
            print("\n" * self.position[1], end="")
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
