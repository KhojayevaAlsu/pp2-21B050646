'''Write a function that accepts string from user 
and print all permutations of that string.'''


from itertools import permutations
def permut(str):
    for i in permutations(str):
        print(" ".join(i))

str = str(input())
permut(str)