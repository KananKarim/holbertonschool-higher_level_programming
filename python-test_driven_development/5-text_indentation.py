#!/usr/bin/python3
""" Text Indentation """


def text_indentation(text):
    """ Text Indent """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in ".:?":
        text = (i + "\n\n").join(
            [line.strip(" ") for line in text.split(i)])

    print("{}".format(text), end="")
