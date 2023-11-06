def lengthOfLastWord(s):
    count = 0 #
    i = len(s) - 1 # 26

    while s[i] == " ":
        i-=1
    while i >= 0 and s[i] !=" ":
        count+=1
        i-=1
    return count

print(lengthOfLastWord("   fly me   to   the moon  "))