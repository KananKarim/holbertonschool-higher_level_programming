#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    nl = list((my_list))
    if idx < 0:
        return nl
    if idx >= len(nl):
        return nl
    nl[idx] = element
    return nl
