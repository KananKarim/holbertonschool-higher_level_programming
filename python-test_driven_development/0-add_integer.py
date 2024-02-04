#!/usr/bin/python3
""" Addition of two integers """


def add_integer(a, b=98):
    """ This function adds two int """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(float("nan")))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
