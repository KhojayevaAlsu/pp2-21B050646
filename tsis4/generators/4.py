'''Implement a generator called squares to yield the square of all numbers from (a) to (b).
 Test it with a "for" loop and print each of the yielded values.'''

import math

a = int(input())
b = int(input())


def squares():
    #x = math.ceil(math.sqrt(a)) - если включительно
    x = int(math.sqrt(a) + 1)
    while(x**2 < b):
        yield x**2
        x += 1


for items in squares():
    print(items)
