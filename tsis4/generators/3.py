'''Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n.
'''

N = int(input())


def generator():
    x = 0
    while(x <= N):
        if(x%3 == 0 and x%4 ==0):
            yield x
        x += 1
    

new_list = []
for items in generator():
    new_list.append(items)
print(new_list)