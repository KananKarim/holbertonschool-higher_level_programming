#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    ld = -1 * (abs(number) % 10)
else:
    ld = number % 10

print("Last digit of {} is {} and is ".format(number, ld), end="")
if ld > 5:
    print("greater than 5")
elif ld == 0:
    print("0")
else:
    print("less than 6 and not 0")
