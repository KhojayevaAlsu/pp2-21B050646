'''Write a Python function that takes a list and returns
 a new list with unique elements of the first list'''

def unique(my_list):
    new_list = []
    new_list.append(my_list[0])
    for  i in range(1, len(my_list)):
        if(my_list[i-1] != my_list[i]):
            new_list.append(my_list[i])
    return new_list

my_list = list(input().split())
print(unique(my_list))