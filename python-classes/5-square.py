#!/usr/bin/python3

""" class Square """

class Square:
    """Représente un carré.

    Attributes:
        size (int): La taille du carré.
    """
    
    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée.

        Args:
            size (int, optional): La taille du carré. Par défaut, c'est 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter pour l'attribut size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter pour l'attribut size.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si la taille n'est pas un entier.
            ValueError: Si la taille est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self._size ** 2

    def my_print(self):
        """Affiche le carré à l'écran avec le caractère #.

        Si la taille est égale à 0, imprime une ligne vide.
        """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)
