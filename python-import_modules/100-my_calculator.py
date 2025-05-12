#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def calculator():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[2] not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, operations(a, b, op)))


def operations(a, b, op):
    if op == '+':
        return add(a, b)

    if op == '-':
        return sub(a, b)

    if op == '*':
        return mul(a, b)

    if op == '/':
        return div(a, b)


if __name__ == "__main__":
    calculator()
