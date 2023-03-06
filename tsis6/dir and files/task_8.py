'''Write a Python program to delete file by specified path.
 Before deleting check for access and whether a given path exists or not.'''

import os
path = input()

if(os.access(path, os.F_OK) == True):
    print("This path exists")
    os.remove(path)
    print("File has been removed")
