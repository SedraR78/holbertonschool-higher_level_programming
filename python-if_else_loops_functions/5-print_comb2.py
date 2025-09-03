#!/usr/bin/python3
for numberOne in range(0, 9):
    for numberTwo in range(0, 9):
        if numberOne != numberTwo and numberOne < numberTwo:
            print(f"{numberOne}{numberTwo} , ", end="")
