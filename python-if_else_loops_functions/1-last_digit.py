#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else number % -10
phrase = ("and is 0" if last_digit == 0 else "and is greater than 5"
          if last_digit > 6 else "and is less than 6 and not 0")
print(f"Last digit of {number} is {last_digit} {phrase}")
