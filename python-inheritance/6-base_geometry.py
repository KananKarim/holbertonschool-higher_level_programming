#!/usr/bin/python3
""" Base Geometry """


class BaseGeometry:
    def __init__(self) -> None:
        """ Init method """
        pass

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")
