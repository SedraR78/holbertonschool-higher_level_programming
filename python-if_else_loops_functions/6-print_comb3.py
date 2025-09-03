#!/usr/bin/python3
for numberOne in range(0, 10):
    for numberTwo in range(0, 10):
        if numberOne != numberTwo and numberOne < numberTwo:
            print(f"{numberOne}{numberTwo}, ", end="")
