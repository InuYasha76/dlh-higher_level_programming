#!/usr/bin/python3
"""This module is about Pascal''s Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n

    Args:
        n (int): the number of rows we want to create
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
        triangle.append(row)
    return triangle
