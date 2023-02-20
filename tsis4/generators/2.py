'''Write a program using generator to print the even numbers between 
0 and n in comma separated form where n is input from console.'''

N = int(input())


def generator():
    x = 0
    while(x <= N):
        if(x%2 == 0):
            yield x
        x += 1
    

new_list = []
for items in generator():
    new_list.append(items)
print(new_list)