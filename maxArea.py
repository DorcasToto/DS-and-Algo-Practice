'''
You are given an integer array height of length n. 

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''

'''
the min value between left and right
area = min * (diff between the indices of the pointers)
store the value somewhere
if the value at left is less than the right move the pointer to right
if the value at right is less than the left move the pointer down
return the max area

'''

def maxArea(height):
    left = 0 # first index 
    right = len(height) - 1 # last index e.g 4
    storedAreas = []

    while left < right:
        currentArea = min(height[left], height[right])  * (right - left)
        storedAreas.append(currentArea)
        if (height[left] < height[right]):
            left+=1
        else:
            right-=1
    return max(storedAreas)

print(maxArea([1,8,6,2,5,4,8,3,7]))