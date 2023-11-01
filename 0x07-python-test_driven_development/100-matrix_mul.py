#!/usr/bin/python3
"""Defines a function that state matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multiply two matrix.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        Either m_a or m_b must be a list
        either m_a or m_b must be a list of lists
        either m_a or m_b should contain only integers or floats
        either m_a or m_b each row must be of the same size
        else TypeError
        either m_a or m_b is empty and can't be multpled
        else ValueError
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(elements, int) or isinstance(elements, float))
               for elements in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elements, int) or isinstance(elements, float))
               for elements in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    column1 = []
    for t in range(len(m_b[0])):
        row1 = []
        for d in range(len(m_b)):
            row1.append(m_b[d][t])
        column1.append(row1)

    new_matrix = []
    for row in m_a:
        row1 = []
        for col in column1:
            prod = 0
            for j in range(len(column1[0])):
                prod += row[j] * col[j]
            row1.append(prod)
        new_matrix.append(row1)

    return new_matrix
