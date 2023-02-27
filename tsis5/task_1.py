'''Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.'''


import re
text = input()
pattern = r"ab*"


if(re.search(pattern, text)):
    print('Found a match!')
else:
    print('No match!')


result = re.findall(pattern, text)
print(result)    
