'''
Given an integer array nums, 

return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
'''

def threeSum(nums):
    i = 0
    j = i+1
    triplets = set()
    for k in range(2,len(nums)):
        if(nums[i] + nums[j] + nums[k]) == 0:
            triplet = (nums[i], nums[j], nums[k])
            triplets.add(triplet)
        i+=1
        j+=1
    return list(triplets)

print(threeSum([-1,0,1,2,-1,-4]))