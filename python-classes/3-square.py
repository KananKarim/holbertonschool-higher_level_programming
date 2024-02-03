#!/usr/bin/python3
""" Square class """


class Square:
    """ Body of Square Class """
    def __init__(self, size=0):
        """ İnitializer method """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calc area method """
        return self.__size ** 2
