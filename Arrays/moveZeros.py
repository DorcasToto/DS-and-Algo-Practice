'''
Check pairs and swap
challenging
'''
def moveZeros(nums):
    l = 0
    for r in range(len(nums)):
        if(nums[r]):
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
    return nums

print(moveZeros([0,1,0,3,12]))
'''
left - 0
right - 1
'''