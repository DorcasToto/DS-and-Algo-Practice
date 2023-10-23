def twoPointer(nums, target):
    storedIndices = {}

    for i in range(len(nums)):
        num = target - nums[i]
        if(num in storedIndices):
           #return the indices
            foundIndices = [storedIndices.get(num),i]
            return foundIndices
            #add the value(nums[i]) to the dictionary
        storedIndices[nums[i]] = i

print(twoPointer([3,2,1,4,3,7],11))
