'''Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625'''


import math


number = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
Area = number*(length**2)/4*math.tan(math.pi/number)
print("The area of the polygon is:", Area)
