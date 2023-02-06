'''Write a function that takes in a list of integers and returns True if it contains 007 in order'''

def spy_game(nums):
    new_list = []
    for i in nums:
        if int(i) == 0 or int(i) == 7:
            new_list.append(int(i))
    return new_list

nums = list(input().split())
if spy_game(nums) == [0, 0, 7]:
    print("True")
else:
    print("False")