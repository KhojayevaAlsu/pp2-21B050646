'''Write a Python program that invoke square root function after specific milliseconds.'''

import time
import math
def root(number) :
    return math.sqrt(number)

number = int(input())
mileseconds = int(input())
result = root(number)
time.sleep(mileseconds/1000)
print("Square root of", number, "after", mileseconds, "miliseconds is", result)