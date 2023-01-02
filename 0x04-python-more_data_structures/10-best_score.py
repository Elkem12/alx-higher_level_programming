#!/usr/bin/python3
<<<<<<< HEAD
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    biggest = max(my_dict.values())
    for key, value in my_dict.items():
        if value is biggest:
            return key
=======


def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader = ""
        for i in my_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                leader = i
        return leader
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
