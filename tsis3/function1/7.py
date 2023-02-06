'''Given a list of ints, return True 
if the array contains a 3 next to a 3 somewhere.'''

def has_33(nums):
    for i in range(len(nums) - 1):
        if int(nums[i]) == 3 and int(nums[i + 1]) == 3:
            return True
    return False


nums = list(input().split())
if has_33(nums) == True:
    print("True")
else:
    print("False")