'''Write a Python program with builtin function that accepts a string and calculate
 the number of upper case letters and lower case letters'''

def counter(str):
    cnt_upper = 0
    cnt_lower = 0
    for i in str:
        if(i >= 'A' and i <= 'Z'):
            cnt_upper += 1
        elif(i >= 'a' and i <= 'z'):
            cnt_lower += 1
    return cnt_upper, cnt_lower


str = input()
print(counter(str))