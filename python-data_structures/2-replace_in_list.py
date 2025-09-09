#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Vérifier si l'index est négatif ou hors de portée
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Remplacer l'élément à la position idx
    my_list[idx] = element
    return my_list
