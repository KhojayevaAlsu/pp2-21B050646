'''Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.'''

import re
text = input()
pattern = r"^a.*b$"


if(re.search(pattern, text)):
    print('Found a match!')
else:
    print('No match!')


result = re.findall(pattern, text)
print(result)   