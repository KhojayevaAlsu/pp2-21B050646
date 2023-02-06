'''Create a python file and import some of the functions from the above 13 tasks and try to use them.'''
def filter_prime(x):
    div = 0
    for i in range(2,x):
        if x%i == 0:
            div += 1
    if div == 0:
        print(x)
    else:
        print("Not prime number")

def histogram(x):
    list = []
    for i in range(x):
        list.append("*")
    print("".join(list))

def volume(r):
    V = 4/3 * (3.14 * r**3)
    return float(V)

a = int(input())
filter_prime(a)
histogram(a)
print(volume(a))

