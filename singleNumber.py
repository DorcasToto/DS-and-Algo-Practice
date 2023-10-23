'''
use set to keep track of every number
'''
# def singleNumber(nums):
#     numbers = set()
#     singleNum = 0
#     for num in nums:
#         if(num in numbers):
#             numbers.remove(num)
#         numbers.add(num)
#     return numbers.pop()


#print(singleNumber([4,1,2,1,2]))
#print(singleNumber([3,2,3,1,1]))
'''
numbers = {2,1}
'''

'''
Approach 2
using ^ - all the elements that appear twice will cancel
'''
def singleNumber(nums):
    singleNum = 0 # n^0 = n
    for num in nums:
        print(singleNum)
        singleNum ^= num
        # singleNum = num ^ singleNum
    return singleNum

print(singleNumber([3,2,3,1,1]))
'''
singleNum = 3
3 ^ 3 = yes,cancel out

'''
