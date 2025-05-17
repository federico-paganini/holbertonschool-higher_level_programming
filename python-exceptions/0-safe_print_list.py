#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    try:
        for i in my_list:
            if cont < x:
                print(f"{i}", end="")
                cont += 1
        print(f"")
    except Exception:
        pass
    return cont
