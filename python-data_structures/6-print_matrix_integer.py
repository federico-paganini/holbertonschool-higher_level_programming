#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        str_row = ""
        for i in range(len(row)):
            str_row += "{:d}".format(row[i])
            str_row += " " if i < len(row) - 1 else ""
        print(str_row)
