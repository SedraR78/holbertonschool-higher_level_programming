#!/usr/bin/python3
for numberOne in range(0, 10):
    for numberTwo in range(0, 10):
        if numberOne != numberTwo and numberOne < numberTwo:
            if numberOne == 8 and numberTwo == 9:
                print("{}{}".format(numberOne, numberTwo))
            else:
                print("{}{}, ".format(numberOne, numberTwo), end="")
