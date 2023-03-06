'''Write a Python program to copy the contents of a file to another file'''

import os
import shutil

file_1 = input()
file_2 = input()
shutil.copy(file_1, file_2)
