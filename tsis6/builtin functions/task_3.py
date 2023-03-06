'''Write a Python program with builtin function that checks whether a passed string is palindrome or not.'''

def is_palindrome(str):
    if(str == str[:: -1]):
        return True
    

str = input()
if(is_palindrome(str) == True):
    print("Is a palindrome")
else:
    print("Is not a palindrome")