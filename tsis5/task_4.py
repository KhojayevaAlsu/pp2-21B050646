'''Write a Python program to find the sequences of one upper case letter followed by lower case letters.'''

import re
text = input()
pattern = r"[A-Z]{1}[a-z]+"


if(re.search(pattern, text)):
    print('Found a match!')
else:
    print('No match!')


result = re.findall(pattern, text)
print(result)   