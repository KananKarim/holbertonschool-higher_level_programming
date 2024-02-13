#!/usr/bin/python3
""" documentation """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ setter method """
        return self.__height

    @width.setter
    def width(self, width):
        """ width setter """
        self.__width = width
        return self.__width

    @height.setter
    def height(self, height):
        """ height setter """
        self.__height = height
        return self.__height
