#!/usr/bin/python3
"""Divide a matrix module"""


def matrix_divided(matrix, div):
    """Write a function that divides all elements of a matrix"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    mtx = matrix
    new_matrix = []
    lenght = len(mtx[0])
    for i in range(0, len(mtx)):
        new_matrix.append([])
        for j in range(0, len(mtx[i])):
            if len(mtx[i]) != lenght:
                raise TypeError("Each row of the matrix \
must have the same size")
            if type(mtx[i][j]) is not int and type(mtx[i][j]) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            new_matrix[i].append(round(mtx[i][j] / div, 2))
    return new_matrix
