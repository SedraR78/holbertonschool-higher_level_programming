#!/usr/bin/python3

"""Creating Parent Classes"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature Flies!")


"""Using Mixin"""


class Dragon(SwimMixin, FlyMixin):
    """Mixin"""
    def roar(self):
        print("The dragon roars!")
