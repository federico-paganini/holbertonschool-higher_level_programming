#!/usr/bin/python3 

def fizzbuzz():
    for i in range (1, 101):
        words = ""
        words += "Fizz" if i % 3 == 0 else ""
        words += "Buzz" if i % 5 == 0 else ""
        print(words if words else i, end=" ")
