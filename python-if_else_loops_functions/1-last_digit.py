#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string1 = 'Last digit of'
string2 = 'is'
string5 = 'and is greater than 5'
string0 = 'and is 0 '
string6 = 'and is less than 6 and not 0'
ldigit = abs(number) % 10

if ldigit > 5:
    print(f"{string1} {number} {string2} {ldigit} {string5}")
elif ldigit == 0:
    print(f"{string1} {number} {string2} {ldigit} {string0}")
elif ldigit != 0 and ldigit < 6:
    print(f"{string1} {number} {string2} {ldigit} {string6}")
 