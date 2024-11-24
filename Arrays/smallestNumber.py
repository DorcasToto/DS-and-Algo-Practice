def smallestNumber(arr):
    smallestNo = arr[0]
    for num in arr:
        if num < smallestNo:
            smallestNo = num
    return smallestNo

print(smallestNumber([7, 2, 5, 3, 9, 1]))