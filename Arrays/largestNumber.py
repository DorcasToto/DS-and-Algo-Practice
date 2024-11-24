def largestNumber(arr):
    largest = arr[0]
    for num in arr:
        print(f"Comparing {num} with current largest {largest}")
        if num > largest:
            largest = num
    return largest

print(largestNumber([3, 1, 4, 1, 5, 9]))