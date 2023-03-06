'''Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt'''

import os
import string
def files():
    for i in string.ascii_uppercase:
        file = open(i + '.txt', 'x')
        file.close()

files() 