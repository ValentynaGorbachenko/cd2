#is paindrom

def isPalindrom(s):
    if len(s)<1:
        return False
    j = len(s)-1
    for i in range(len(s)//2):
        if s[i] == s[j]:
            j -=1
        else:
            return False
    return True
    

print(isPalindrom('recalacer'))
