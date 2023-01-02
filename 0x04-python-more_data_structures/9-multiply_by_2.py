#!/usr/bin/python3
<<<<<<< HEAD
def multiply_by_2(my_dict):
    tmp_dict = my_dict.copy()
    for x in tmp_dict.keys():
        tmp_dict[x] *= 2
    return (tmp_dict)
=======


def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict.update({key: (value * 2)})
    return new_dict
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
