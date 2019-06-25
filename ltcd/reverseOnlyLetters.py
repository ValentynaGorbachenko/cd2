'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
'''
def reverseOnlyLetters(S):
    l = ""
    r = [None]*len(S)

    # add not letters

    for i, char in enumerate(S):
        if char.isalpha():
            l+=char
        else:
            r[i] = char

    # print(l, r)

    # add leters 
    j=len(l)-1
    for i in range(len(r)):
        if r[i] == None:
            r[i] = l[j]
            j-=1

    # print("".join(r))
    return("".join(r))


def reverseOnlyLetters2(S):
    r =  ['']*len(S)

    i, j = len(S)-1, 0

    while i >=0 and j < len(S):
        if S[i].isalpha():
            r[j] = S[i]
        else:
            while not S[j].isalpha():
                j+=1
                if j >=len(S):
                    j-=1
                    break
            if j < len(S):
                r[j] = S[i]
            
        i-=1
        j+=1

    print("".join(r))

    return "".join(r)

reverseOnlyLetters("21-a_bc1=")








