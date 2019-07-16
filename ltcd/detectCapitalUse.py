'''
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''

def detectCapitalUse(word):
    # check if all caps
    if word.isupper():
        return True

    # check if all lower
    if word.islower():
        return True

    # if at least one character in the word  
    if len(word)>=1:
        # if first character is upper 
        if word[0].isupper():
            # check if the rest is lower 
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
            # if all is lower return true
            else:
                return True
        # if first is not upper return false because all upper and all lower cheked above 
        else:
            return False



print(detectCapitalUse("USA"))
print("USA*"*8)
print(detectCapitalUse("some words"))
print("some words*"*8)
print(detectCapitalUse("Right"))
print("Right*"*8)
print(detectCapitalUse("wrOng"))
print("wrOng*"*8)
print(detectCapitalUse("A"))
print("A*"*8)
print(detectCapitalUse("b"))
print("b*"*8)
print(detectCapitalUse(""))


