#!/usr/bin/python3
for letter in range(97, 123):
     if letter not in (101, 112):
        print("{}".format(chr(letter)), end="")
    