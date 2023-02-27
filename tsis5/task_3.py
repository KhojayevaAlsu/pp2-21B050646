'''Write a Python program to find sequences of lowercase letters joined with a underscore.'''
import re
text = input()
pattern = r"[a-z]\S*_\S*[a-z]"


if(re.search(pattern, text)):
    print('Found a match!')
else:
    print('No match!')


result = re.findall(pattern, text)
print(result)   