#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Body of rectangle class """
    def __init__(self, width=0, height=0):
        """ İnitilazier method """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
