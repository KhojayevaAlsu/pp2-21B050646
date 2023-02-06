'''Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.'''


class Prime:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter(self):
        Primes = list(filter(lambda x: prime(x), self.numbers))
        print(Primes)
def prime(x):
    count = 0
    y = int(x)
    for i in range(2,y):
        if y%i == 0:
            count += 1
    if count == 0:
        return y  


numbers = list(input().split())
prime_numbers = Prime(numbers)
prime_numbers.filter()