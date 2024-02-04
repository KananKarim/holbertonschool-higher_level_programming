#!/usr/bin/python3
""" Matrix division """


def matrix_divided(matrix, div):
    """ Matrix divided """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not all(isinstance(i, list) and
                all(isinstance(j, (int, float)) for j in i) for i in matrix)):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(j / div, 2) for j in i] for i in matrix]


if __name__ == "__main__":
    matrix = [
        (1, 2, 3),
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 2))
    print(matrix)
