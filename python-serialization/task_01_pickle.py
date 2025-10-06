#!/usr/bin/env python3
"""
Module for pickling custom Python objects
"""

import pickle


class CustomObject:
    """A custom Python class that can be serialized and deserialized using pickle"""
    
    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize the CustomObject with name, age, and is_student attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """Display the object's attributes in a formatted way"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename: str):
        """
        Serialize the current instance and save it to the provided filename
        
        Args:
            filename (str): The filename to save the serialized object to
            
        Returns:
            None: Returns None if serialization fails
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PickleError) as e:
            print(f"Error during serialization: {e}")
            return None
    
    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize an instance from the provided filename
        
        Args:
            filename (str): The filename to load the serialized object from
            
        Returns:
            CustomObject or None: Returns the deserialized object or None if deserialization fails
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Error: Deserialized object is not of type CustomObject")
                    return None
        except (FileNotFoundError, IOError, pickle.PickleError, EOFError) as e:
            print(f"Error during deserialization: {e}")
            return None
