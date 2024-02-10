#!/usr/bin/python3
""" document """


def append_write(filename="", text=""):
    """ append_write function """

    with open(filename, "a") as file:
        file.write(text)

    return len(text)
