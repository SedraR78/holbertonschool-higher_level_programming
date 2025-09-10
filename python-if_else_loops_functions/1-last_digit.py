#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string1 = 'Last digit of'
string2 = 'is'
string5 = 'and is greater than 5'
string0 = 'and is 0'
string6 = 'and is less than 6 and not 0'
sl = "\n"

ldigit = abs(number) % 10  # Dernier chiffre positif
ldigit_display = ldigit if number >= 0 else -ldigit  # Afficher ldigit avec le signe approprié

if ldigit > 5:
    print(f"{string1} {number} {string2} {ldigit_display} {string5}")
elif ldigit == 0:
    print(f"{string1} {number} {string2} {ldigit_display} {string0}")
else:  # ldigit < 6
    print(f"{string1} {number} {string2} {ldigit_display} {string6}")
