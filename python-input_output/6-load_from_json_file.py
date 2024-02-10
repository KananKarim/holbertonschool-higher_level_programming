#!/usr/bin/python3
""" document """
import json


def load_from_json_file(filename):
    """ JSON TO IBJ """

    with open(filename) as f:
        return json.loads(f.read())
