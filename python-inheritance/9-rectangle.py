#!/usr/bin/python3
""" doc """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ init method """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ str method """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ area method """
        return self.__width * self.__height
