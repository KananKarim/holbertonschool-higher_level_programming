#!/usr/bin/python3
""" doc """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ init method """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
