#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is positive" if number > 0 else f"{number} is negative")
