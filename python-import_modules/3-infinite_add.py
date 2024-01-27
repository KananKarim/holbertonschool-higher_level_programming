#!/usr/bin/python3

from sys import argv


def sumargs():
    sum = 0
    if len(argv) == 1:
        print(sum)
        return
    argv.pop(0)
    for i in range(len(argv)):
        sum += int(argv[i])

    print(sum)


if __name__ == "__main__":
    sumargs()
