#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age 
        self.is_student = is_student

    def display(self):
        print(f"{self.name}  {self.age} , {self.is_student}")


    def serialize_and_save_to_file(data, filename):

        with open(filename, 'wb') as file:
            pickle.dump(data, file)
