'''Write a python program to convert snake case string to camel case string'''


import re
text = input()
camel_case = re.split('_', text)


for i in camel_case:
    for j in range(len(i)):
        if(j == 0):
            print(i[j].upper(), end = '')
        else:
            print(i[j], end = '')  



   