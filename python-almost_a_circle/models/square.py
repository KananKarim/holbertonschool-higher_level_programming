#!/usr/bin/python3
""" documentation """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str function """
        return f"[{__class__.__name__}] ({self.id})\
 {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ getter """
        return self.width

    def to_dictionary(self):
        """ to dictionary """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    @size.setter
    def size(self, value):
        """ setter """
        super().validation("width", value, True)
        super().validation("height", value, True)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
