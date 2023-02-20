'''Implement a generator that returns all numbers from (n) down to 0.'''

N = int(input())


def generator():
    x = N - 1
    while(x >= 0):
        yield x
        x -= 1
    

for items in generator():
    print(items)