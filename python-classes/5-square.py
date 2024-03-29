#!/usr/bin/python3
""" Square class """


class Square:
    """ Body of the class """
    def __init__(self, size):
        """ Initilazier method """
        self.__size = size

    @property
    def size(self):
        """ getter size meth """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter size meth """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area of square """
        return self.__size ** 2

    def my_print(self):
        """ my_print method """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
