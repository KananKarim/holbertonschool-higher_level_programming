#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    sum = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_string) == 1:
        sum += rom[roman_string]
        return sum

    for i in range(len(roman_string) - 1):
        if rom[roman_string[i]] < rom[roman_string[i + 1]]:
            sum -= rom[roman_string[i]]
        else:
            sum += rom[roman_string[i]]
    sum += rom[roman_string[-1]]
    return sum
