#!/usr/bin/python3
""" Mylist class """


class MyList(list):
    """ body of the class """
    def print_sorted(self):
        print(sorted(self))
