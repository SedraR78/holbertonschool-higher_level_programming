#!/usr/bin/python3
"""Extending the python list """
class VerboseList(list):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        super().__init__(iterable)
        
    def append(self, object):
        super().append(object)
        print(f"Added {object} to the list.")
    
    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")
    
    def remove(self, value):
        super().remove(value)
        print(f"Removed {value} from the list.")
        
    
    def pop(self, index = -1):
        object = super().pop(index)
        print(f"Popped {object} from the list.")
        return object


