'''Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and directory portion of the given path.'''

import os
path = input()

if(os.access(path, os.F_OK) == True):
    print("filename:", os.path.basename(path))
    print("directory:", os.path.dirname(path))
else:
    print("This path does not exist")