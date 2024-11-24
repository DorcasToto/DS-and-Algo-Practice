def smallestLargestNumber(arr):
    newArr = set(arr)
    smallest = min(newArr) 
    largest = max(newArr)  
    return smallest, largest
    

print(smallestLargestNumber([7, 2, 5, 3, 9, 1, 7, 5]))