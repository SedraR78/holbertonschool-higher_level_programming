#!/usr/bin/python3
for num in range(0, 100):
    if 0 <= num < 10:
        print(f"0{num},", end="")
    else:
        print(f"{num},", end="")
