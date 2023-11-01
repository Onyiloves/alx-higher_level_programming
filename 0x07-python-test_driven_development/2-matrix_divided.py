#!/usr/bin/python3
# 2-matrix_divided.py
"""function that div all elements of a same size matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        matrix must be a matrix (list of lists) of integers/floats.
        Each row of the matrix must have the same size.
        div must be a number.
        else TypeError
        div can’t be equal to 0,except division by zero
        else ZeroDivisionError
        elements of the matrix should be divided by div in 2 d.p
    Returns:
        A new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elements, int) or isinstance(elements, float))
                    for elements in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
