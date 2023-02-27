'''Write a Python program to replace all occurrences of space, comma, or dot with a colon.'''

import re
text = input()
pattern = r"[., ]"



result = re.sub(pattern,':', text)
print(result)   