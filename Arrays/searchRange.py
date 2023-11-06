def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    targetValue = {}
    if len(nums) == 0:
        return [-1, -1]

    for i in range(len(nums)):
        if nums[i] - target == 0:
            if nums[i] in targetValue:
                foundValues = [targetValue.get(nums[i]), i]                
                return foundValues
        targetValue[nums[i]] = i
        print(targetValue)

result = searchRange([5,7,7,8,8,10], 8)
print(result)