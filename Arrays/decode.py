
def decode(encoded, first):
    arr = [first]

    for num in encoded:
        nextElement = num ^ arr[-1]
        arr.append(nextElement)
    return arr
    
        # 6 = 4 ^ x
        # x = 6 ^ 4


#     arr = [first] # the first element in the array

#     for num in encoded:
#         nextElement = arr[-1] ^ num
#         arr.append(nextElement)
#     return arr

encoded = [1, 2, 3]
first = 1
result = decode(encoded, first)
print(result)

'''
Suppose arr is [1, 0, 2, 1] and encoded is [1, 2, 3]. We start with first as 1.
encoded[i] = arr[i] XOR arr[i + 1]
[6,2,7,3]

next_element = 1 ^ 1, which is 0.
next_element = 0 ^ 2, which is 2.
next_element = 2 ^ 3, which is 1.

'''