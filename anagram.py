def isAnagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    char_count = {}
    for char in word1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in word2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    
    if sum(char_count.values()) == 0:
        return True
    return False

print(isAnagram("listen","silent"))