'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
def containDuplicate(nums):
    unique_set = set()
    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)
    return False