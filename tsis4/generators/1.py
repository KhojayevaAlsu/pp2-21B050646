'''Create a generator that generates the squares of numbers up to some number N.'''

N = int(input())



def generator():
    x = 1
    while(x**2 <= N):
        yield x**2
        x += 1


for items in generator():
    print(items)