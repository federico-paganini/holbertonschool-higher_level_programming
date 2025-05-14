#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_val = my_list[0]
    for i in my_list[1:]:
        if my_list[i] > max_val:
            max_val = my_list[i]

    return max_val
