from collections import deque
def isValid(s):
    stack = deque()
    charMap = {
            ']':'[',
            ')':'(',
            '}':'{'
            }

    for char in s:
        if char in charMap:
            if stack and stack[-1] == charMap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


si = '()[]{}'
print(isValid(si))