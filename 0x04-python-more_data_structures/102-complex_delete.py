#!/usr/bin/python3
<<<<<<< HEAD
def complex_delete(my_dict, value):
    targets = []
    for key, key_value in my_dict.items():
        if key_value is value:
            targets.append(key)
    for x in targets:
        del my_dict[x]
    return(my_dict)
=======


def complex_delete(a_dictionary, value):
    """
    A function that computes the square value of
    all integers of a matrix using map
    """
    a_list = list(a_dictionary.keys())
    for key in a_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
