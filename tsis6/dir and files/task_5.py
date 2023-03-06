'''Write a Python program to write a list to a file.'''

import os

file_name = input()

file = open(file_name + '.txt', 'a')
text = list(input("Write a list:").split())
file.writelines(text)
file.close()
print("File has been changed")
print(text)
