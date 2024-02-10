#!/usr/bin/python3
""" document """


def write_file(filename="", text=""):
    """ write_file function """

    with open(filename, "w", encoding="utf-8") as writer:
        writer.write(text)
    return len(text)
