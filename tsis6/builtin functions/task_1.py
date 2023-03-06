'''Write a Python program with builtin function to multiply all the numbers in a list'''

def multiply(list):
    result = 1
    for i in list:
        result = int(i)*result
    return result

list = input().split()
print(multiply(list))