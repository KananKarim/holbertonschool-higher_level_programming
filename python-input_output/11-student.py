#!/usr/bin/python3
""" documentation """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ init method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json """
        if isinstance(attrs, list) and\
                all(isinstance(it, str) for it in attrs):
            new_dict = {}
            for el in attrs:
                if self.__dict__.get(el):
                    new_dict[el] = self.__dict__[el]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ replace the instance attributes with json """
        for key, value in json.items():
            setattr(self, key, value)
