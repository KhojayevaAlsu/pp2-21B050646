'''Define a functino histogram() that takes a list of integers and prints a histogram to the screen.'''

def histogram(x):
    list = []
    for i in range(x):
        list.append("*")
    print("".join(list))


nums = list(input().split())
for i in nums:
    histogram(int(i))