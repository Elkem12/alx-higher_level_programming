#!/usr/bin/python3
<<<<<<< HEAD
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    res = 0
    res2 = 0
    for x, y in my_list:
        res += x * y
        res2 += y
    return (res / res2)
=======


def weight_average(my_list=[]):
    """
    A function that returns the weighted
    average of all integers tuple
    """
    weighted_avg = 0
    size = 0
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    for tup in my_list:
        weighted_avg += (tup[0] * tup[1])
        size += tup[1]
    return (weighted_avg / size)
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
