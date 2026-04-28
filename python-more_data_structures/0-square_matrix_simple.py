#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return []
    return [[val ** 2 for val in row] for row in matrix]
