#!/usr/bin/python3
from sys import argv

def args():
    if len(argv) == 1:
        print("0 arguments.")
        return
    if len(argv) == 2:
        print("1 argument")
        print("1: {}".format(argv[1]))
        return
    argv.pop(0)
    print("{} arguments:".format(len(argv)))
    counter = 0
    for item in argv:
        counter += 1
        print("{}: {}".format(counter, item))
        
if __name__ == "__main__":
    args()
