def findMaxK(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    seen = set()
    res = 0
    for i in range(len(nums)):
        if(-1 * nums[i]) in nums:
            seen.add(nums[i])
            res = max(res, abs(nums[i]))
    if(res == 0):
        return -1
    return res

print(findMaxK([-1,2,-3,3, 4, -4 , 5, -5 ]))