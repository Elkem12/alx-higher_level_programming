#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    saved_nums = []

    for num in my_list:

        if num in saved_nums:
            continue
        else:
            result += num
            saved_nums.append(num)

    return result
