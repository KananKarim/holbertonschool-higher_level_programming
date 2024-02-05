#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Body of rectangle class """
    def __init__(self, width=0, height=0):
        """ İnitilazier method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of rectangle """
        return (self.__width + self.__height) * 2
