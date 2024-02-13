#!/usr/bin/python3
""" documentation """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert to json """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write(json.dumps([]))
                return
            list_objs = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_objs))
