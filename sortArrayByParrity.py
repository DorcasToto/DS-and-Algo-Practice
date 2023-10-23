def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0
    # right =  len(nums) - 1

    # while left < right:
    #     if(nums[left] % 2 != 0):
    #         nums[left], nums[right] = nums[right],nums[left]
    #         right -= 1
    #     else:
    #         left+=1
    # return nums

    for right in range(len(nums)):
        if(nums[right] % 2 == 0) :
            nums[left], nums[right] = nums[right],nums[left]
            left+=1
    return nums


print(sortArrayByParity([4, 3,1,2,4]))