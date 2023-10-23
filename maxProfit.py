def maximumProfit(nums):
    left = 0
    maxProfit = 0

    for i in range(1,len(nums)):
        if(nums[i] - nums[left]) > 0:
            maxProfit += nums[i] - nums[left]
        left+=1
    return maxProfit
print(maximumProfit([7,1,5,3,6,4]))


'''
[1,2,3,4,5]
left++
++left

'''
