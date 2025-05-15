#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_list = []
    for num in my_list:
        bool_list.append(True if num % 2 == 0 else False)
    return bool_list
