'''Write a Python program to check for access to a specified path.
 Test the existence, readability, writability and executability of the specified path'''

import os
path = input()

if(os.access(path, os.F_OK) == True):
    print("This path exists")
else:
    print("This path does not exist")


if(os.access(path, os.R_OK) == True):
    print("This path is readable")
else:
    print("This path is not readable")


if(os.access(path, os.W_OK) == True):
    print("This path is writable")
else:
    print("This path is not writable")


if(os.access(path, os.R_OK) == True):
    print("This path is executable")
else:
    print("This path is not executable")
