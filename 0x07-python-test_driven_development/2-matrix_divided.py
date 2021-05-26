#!/usr/bin/python3
"""
Module that divide a matrix
checks for integers and floats
te list must have the same size
"""


def matrix_divided(matrix, div):
    """
    return a new matrix with integers or floats
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    size = len(matrix[0])
    te = "matrix must be a matrix (list of lists) of integers/floats"
    for lt in matrix:
        aux = []
        if size == len(lt):
            for num in lt:
                if type(num) is int or type(num) is float:
                    aux.append(round(num / div, 2))
                else:
                    raise TypeError(te)
            new_matrix.append(aux)
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
