'''Write a Python program with builtin function that returns True if all elements of the tuple are true.'''

mytuple = tuple(input().split())
mylist = []


for i in mytuple:
    if i == 'False':
        mylist.append(False)
    elif i == 'True':
        mylist.append(True) 
    elif i == '0':
        mylist.append(0)
    else:
        mylist.append(i)


def check(mylist):
    x = all(mylist)
    print(x)


check(mylist)