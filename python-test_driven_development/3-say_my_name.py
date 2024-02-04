#!/usr/bin/python3
""" Say my name! """


def say_my_name(first_name, last_name=""):
    """ body of say_my_name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    say_my_name("ds", "Smith")
    say_my_name("Walter", "White")
    say_my_name()
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
