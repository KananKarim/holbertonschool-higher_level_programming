#!/usr/bin/python3
""" documentation """


def read_file(filename=""):
    """ read_file method """

    with open(filename, encoding="utf-8") as reader:
        print(reader.read(), end="")
