'''Write a Python program to insert spaces between words starting with capital letters.'''


import re
text = input()
pattern = r'[A-Z][^A-Z]*'
result = re.findall(pattern, text)
for i in result:
    print(i, end = " ")