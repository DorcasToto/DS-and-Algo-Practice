'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''

def squareArrays(nums):
    left = 0 #-4
    right = len(nums) - 1 # 10
    squaredArray = [0 for _ in range(len(nums))]
    numberToTrack = len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            squaredArray[numberToTrack] = (nums[left] ** 2)
            left+=1
        else:
            squaredArray[numberToTrack] = (nums[right] ** 2)
            right-=1
        numberToTrack-=1
    return squaredArray



print(squareArrays([-4, -1, 0, 3, 10]))


'''
[-4,-1,0,3,10]
[16,2,0,9,10]
'''
