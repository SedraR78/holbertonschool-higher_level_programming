#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.size = size

    def my_print(self):
        if self.size <= 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)
