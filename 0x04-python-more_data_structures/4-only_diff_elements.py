#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    uni = set_1.union(set_2)
    list = []
    for x in uni:
        list.append(x)
    return list
