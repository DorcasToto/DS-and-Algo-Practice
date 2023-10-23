'''
1. initialize an empty set
2. loop through the array nums
3. check if the num * 2 is inside the set
4. if its there return true
5. if not return add the num to the set
example check if 5 and 10 exists in [10,2,5,3]
'''
def doubleExist(nums):
    doubleNumbers = set()
    for num in nums:
        if(num * 2) in doubleNumbers:
            return True
        doubleNumbers.add(num)
    return False


#print(doubleExist([10,2,5,3]))
# 10,2

'''
use hashmap
'''
def doubleExist(nums):
    doubleNumbers = {}
    for i in range(len(nums)):
        if((nums[i]) * 2) in doubleNumbers:
            return True
        doubleNumbers[nums[i]] = i
        print(doubleNumbers)
    return False


print(doubleExist([10,2,5,3]))
