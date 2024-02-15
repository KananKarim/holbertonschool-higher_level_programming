#!/usr/bin/python3
""" documentation """
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(21, 12)
        if cls.__name__ == "Square":
            dummy = cls(21)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        cls_name = cls.__name__
        if not os.path.isfile(f"{cls_name}.json"):
            return []
        with open(f"{cls_name}.json", "r") as file:
            obj = cls.from_json_string(file.read())
            for i in range(len(obj)):
                obj[i] = cls.create(**obj[i])
        return obj
