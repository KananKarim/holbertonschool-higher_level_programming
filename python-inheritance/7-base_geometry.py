#!/usr/bin/python3
""" Base Geometry """


class BaseGeometry:
    """ body of the class """
    def __init__(self) -> None:
        """ Init method """
        pass

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validation of integer """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
