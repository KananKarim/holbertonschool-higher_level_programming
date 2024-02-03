#!/usr/bin/python3
""" Square class """


class Square:
    """ Body of class """
    def __init__(self, size=0):
        """ İnitializer method """
        self.__size = size

    @property
    def size(self):
        """ getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area of square """
        return self.__size ** 2
