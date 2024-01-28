#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    return (ln, sentence[0] if sentence else None)
