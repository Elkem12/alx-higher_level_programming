#!/usr/bin/python3
<<<<<<< HEAD
def search_replace(my_list, search, replace):
    return (list(map(lambda x: replace if x is search else x, my_list)))
=======


def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences
    of an element by another in a new list
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
