#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string1 = 'Last digit of'
string2 = 'is'
string5 = 'and is greater than 5'
string0 = 'and is 0'
string6 = 'and is less than 6 and not 0'
sl = "\n"

ldigit = number % 10  # Get the last digit, keeping the sign

# Determine the correct display value for ldigit
if number < 0 and ldigit != 0:
    ldigit_display = -ldigit
else:
    ldigit_display = ldigit

if ldigit_display > 5:
    print(f"{string1} {number} {string2} {ldigit_display} {string5}")
elif ldigit_display == 0:
    print(f"{string1} {number} {string2} {ldigit_display} {string0}")
else:  # When ldigit_display < 6
    print(f"{string1} {number} {string2} {ldigit_display} {string6}")
