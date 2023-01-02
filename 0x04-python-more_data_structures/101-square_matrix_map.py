#!/usr/bin/python3
def square_matrix_map(matrix=[]):
<<<<<<< HEAD
    return (list(map(lambda r: list(map(lambda x: x**2, r)), matrix)))
=======
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
