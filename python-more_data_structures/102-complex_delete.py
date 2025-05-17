#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    remove_items = list(
        key for key, val in a_dictionary.items()
        if val == value
    )
    for key in remove_items:
        a_dictionary.pop(key)

    return a_dictionary
