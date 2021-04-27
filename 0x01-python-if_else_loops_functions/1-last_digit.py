#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ld = number % 10
else:
    ld = number % -10
string = "Last digit of {:d} is {:d}".format(number, ld)
if ld > 5:
    print(string, "and is greater than 5")
elif ld == 0:
    print(string, "and is 0")
else:
    print(string, "and is less than 6 and not 0")
