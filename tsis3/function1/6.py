'''Write a function that accepts string from user, 
return a sentence with the words reversed. 
We are ready -> ready are We
'''


def reverse(str) :
    print(" ".join(str[:: -1]))


str = input().split()
reverse(str)