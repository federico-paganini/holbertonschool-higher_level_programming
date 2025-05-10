#!/usr/bin/python3

def remove_char_at(str, n):
    str_dup = ""
    for i in range(len(str)):
        if i != n:
            str_dup += str[i]
    
    return str_dup
