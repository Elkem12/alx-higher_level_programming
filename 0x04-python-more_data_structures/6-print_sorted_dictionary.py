#!/usr/bin/python3
<<<<<<< HEAD
def print_sorted_dictionary(my_dict):
    for keys in sorted(my_dict.keys()):
        print('{}: {}'.format(keys, my_dict[keys]))
=======


def print_sorted_dictionary(a_dictionary):
    """
    A function that prints a dictionary by ordered keys
    """
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
