#!/usr/bin/python3
<<<<<<< HEAD
def uniq_add(my_list=[]):
    return(sum(set(my_list)))
=======


def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    new_list = []
    sum = 0
    for num in my_list:
        if num not in new_list:
            sum += num
            new_list.append(num)
    return sum
>>>>>>> d51a6f843d2812c4098d3414f69a335eccc1451d
