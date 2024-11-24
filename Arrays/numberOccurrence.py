def numberOccurence(arr, num):
    count = 0
    for n in arr:
        if(n == num):
            count +=1
    return count

print(numberOccurence([1, 2, 3, 1, 1, 4, 5, 5], 5))