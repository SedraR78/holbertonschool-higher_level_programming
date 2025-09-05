#!/usr/bin/python3
import random
number = random.randint(-10, 10)
space = " "
if number > 0:
    print(f"{number}{space}is positive")
elif number < 0:
    print(f"{number}{space}is negative")
else:
    print(f"{number}{space}is zero")
