def isPalindrome(s):
    '''
    move to the middle of the string
    check if the left characters equate the right characters
    is palindrome true
    '''
    newString = s.replace(" ", "").replace(",", "").replace(":", "").lower()
    print(len(newString) // 2)
    for i in range(0, len(newString) // 2):
        if(newString[i] != newString[len(newString) -i - 1]):
            return False
    return True
print(isPalindrome("race a car"))