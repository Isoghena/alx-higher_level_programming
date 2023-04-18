#!/usr/bin/python3
"""Module that divides all elements of a matrix of similiar rows."""


def matrix_divided(matrix, div):
    """Function returns new matrix with each divided element by div"""
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    new = []
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(error_msg)
    if type(div) is int or type(div) is float or div is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(error_msg)
    for i in range(len(matrix)):
        if len(matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have same size")
        new.append([])
        for j in matrix[i]:
            if type(j) is int or type(j) is float:
                new[i].append(round(j / div, 2))
            else:
                raise TypeError(error_msg)
    return new
