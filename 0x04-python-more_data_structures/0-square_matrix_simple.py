#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    row1 = []
    row2 = []
    row3 = []
    
    matrix2 = matrix[:]

    for row in range(0, len(matrix2)):
        for col in range(0, len(matrix2[row])):
            col_val = matrix2[row][col]
            col_val = col_val ** 2
            row1.append(col_val)

    for _ in range(0, len(row1)):
        row2.append(row1[_])
        if (_ + 1) % 3 == 0:
            row3.append(row2)
            row2 = []

    return row3
