#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element ** 2)
        newMatrix.append(squared_row)
    return newMatrix
