#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Initialisation de l'itérateur
        self.count = 0  # Compteur pour le nombre d'éléments itérés

    def get_count(self):
        return self.count  # Retourne le nombre d'éléments itérés

    def __next__(self):
        try:
            item = next(self.iterator)  # Récupère le prochain élément
            self.count += 1  # Incrémente le compteur
            return item  # Retourne l'élément récupéré
        except StopIteration:
            raise StopIteration  # Lève une exception si plus d'éléments

