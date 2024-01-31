#!/usr/bin/python3
def common_elements(set_1, set_2):
    return [i1 for i1 in set_1 for i2 in set_2 if i1 == i2]
