#!/usr/bin/python3

class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature Flies!")

class Dragon(SwimMixin,FlyMixin):
    def roar(self):
        print("The dragon roars!")

