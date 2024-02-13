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

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id})\
 {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @property
    def height(self):
        """ setter method """
        return self.__height

    def to_dictionary(self):
        """ to dictionary """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def area(self):
        """ area method """
        return self.__height * self.__width

    def validation(self, name, input, check):
        """ validation function """
        if not isinstance(input, int):
            raise TypeError(f"{name} must be an integer")
        if input <= 0 and check:
            raise ValueError(f"{name} must be > 0")
        if input < 0 and not check:
            raise ValueError(f"{name} must be >= 0")

    def update(self, *args, **kwargs):
        """ update function """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, v in enumerate(args):
                setattr(self, attributes[i], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def display(self):
        """ display method """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    @width.setter
    def width(self, width):
        """ width setter """
        self.validation("width", width, True)
        self.__width = width
        return self.__width

    @x.setter
    def x(self, x):
        """ x setter """
        self.validation("x", x, False)
        self.__x = x
        return self.__x

    @y.setter
    def y(self, y):
        """ y setter """
        self.validation("y", y, False)
        self.__y = y
        return self.__y

    @height.setter
    def height(self, height):
        """ height setter """
        self.validation("height", height, True)
        self.__height = height
        return self.__height
