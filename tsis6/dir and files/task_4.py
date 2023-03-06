'''Write a Python program to count the number of lines in a text file.'''

import os

file = input()
cnt = 0

file_text = open(file, 'r')
for i in file_text:
    cnt += 1
file_text.close()

print(cnt)