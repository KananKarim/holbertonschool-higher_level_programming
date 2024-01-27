#!/usr/bin/python3

import hidden_4


def showHiddenFiles():
    for file in dir(hidden_4):
        if file.startswith("__"):
            continue
        print("{}".format(file))


if __name__ == "__main__":
    showHiddenFiles()
