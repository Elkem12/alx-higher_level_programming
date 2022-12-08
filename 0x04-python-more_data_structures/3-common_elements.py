#!/usr/bin/python3

def common_elements(set_1, set_2):
    sorted_set = set_1.intersection(set_2)
    list = []
    for x in sorted_set:
        list.append(x)
    return list    
    
