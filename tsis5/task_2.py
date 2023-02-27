'''Write a Python program that matches a string that has an 'a' followed by two to three 'b'.'''


import re
text = input()
pattern = r"ab{2,3}"


if(re.search(pattern, text)):
    print('Found a match!')
else:
    print('No match!')


result = re.findall(pattern, text)
print(result)   