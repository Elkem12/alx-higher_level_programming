#!/usr/bin/python3

from is_negative import is_negative
from is_out_of_range import is_out_of_range


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if is_out_of_range(idx, my_list) or is_negative(idx):
        return new_list

    new_list[idx] = element

    return new_list
