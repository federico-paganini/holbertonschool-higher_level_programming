#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0 if len(tuple_a) == 0 else tuple_a[0]
    a += 0 if len(tuple_b) == 0 else tuple_b[0]
    b = 0 if len(tuple_a) == 1 else tuple_a[1]
    b += 0 if len(tuple_b) == 1 else tuple_b[1]
    tuple_res = a, b
    return tuple_res
