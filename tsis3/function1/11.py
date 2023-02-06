'''Write a Python function that checks whether a word or phrase is palindrome'''

def is_palindrome(str):
    if str == str[:: -1]:
        return True
    else:
        return False

str = str(input())
if is_palindrome(str) == True:
    print("Palindrome")
else:
    print("Not a palindrome")