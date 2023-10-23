'''
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Steps
1. pointers
2. 

'''
def rescueBoat(nums, limit):
    left = 0 # first index 
    right = len(nums) - 1 # last index e.g 4
    count = 0
    nums.sort()

    while left <= right :
        if(nums[left] + nums[right] <= limit):
            left+=1
        right -=1
        count +=1
    return count

nums = [3, 2, 2, 1]
limit = 3
# print(rescueBoat(nums, limit))

#wrong
def rescueBoat(nums, limit):
    left = 0 # first index 
    count = 0
    nums.sort()

    for i in range(1, len(nums)):
        if(nums[left] + nums[i] <= limit):
            left+=1
        count +=1
    return count

nums = [3,5,3,4]
limit = 5
print(rescueBoat(nums, limit))

'''
[3,2,2,1], limit = 6
output 3
[1,1,3, 2, 3]
'''