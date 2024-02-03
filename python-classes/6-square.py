#!/usr/bin/python3
""" Square class """


class Square:
    """ Body of the class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initilazier method """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter of size """
        return self.__size

    @property
    def position(self):
        """ getter of position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter of position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """ setter of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area of square """
        return self.__size ** 2

    def my_print(self):
        """ print func """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
