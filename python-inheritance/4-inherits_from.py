#!/usr/bin/python3
""" check inherit """


def inherits_from(obj, a_class):
    """ inherit function """
    return isinstance(obj, a_class) and type(obj) is not a_class
