#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ret_value = None
    try:
        ret_value = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)

    return ret_value
