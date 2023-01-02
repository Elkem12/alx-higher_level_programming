#!/usr/bin/python3
<<<<<<< HEAD
def square_matrix_simple(matrix=[]):
    tmp = []
    for x in matrix:
        tmp.append(list(map(lambda x: x**2, x)))
    return (tmp)
=======


def square_matrix_simple(matrix=[]):
    """
    wordA function that computes the square
    value of all integers of a matrix.
    """
    new_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        new_matrix.append(result)
    return new_matrix
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
