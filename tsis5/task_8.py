'''Write a Python program to split a string at uppercase letters.'''


import re
text = input()
pattern = r'[A-Z][^A-Z]*'
result = re.findall(pattern, text)
print(result)


