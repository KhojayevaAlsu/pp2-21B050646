'''You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers 
as an agrument and returns only prime numbers from the list.'''


def filter_prime(x):
    div = 0
    for i in range(2,x):
        if x%i == 0:
            div += 1
    if div == 0:
        print(x)


my_list = list(input().split())

for i in my_list:
    filter_prime(int(i))
    
