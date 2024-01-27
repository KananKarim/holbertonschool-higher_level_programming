#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    ld = -1 * (abs(number) % 10)
else:
    ld = number % 10

if ld == 0:
    print("Last digit of {} is {} and is 0".format(number, ld))
elif ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, ld))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
            .format(number, ld))
