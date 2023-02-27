'''Write a Python program to convert a given camel case string to snake case.'''

import re
text = input()
t = re.sub('(.)([A-Z])', r"\1_\2", text)
snake_case = re.sub('([A-Z])([A-Z])', r"\1_\2", t)
print(snake_case.lower())