#!/usr/bin/python3
""" documentation """


def read_file(filename=""):
    """ read_file method """

    with open(filename) as reader:
        print(reader.read())
