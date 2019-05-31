'''
You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of 
stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

def j_and_s(str_j, str_s): 
    count =0 
    for j in str_j:
        for s in str_s:
            # print ("j is ", j, "is is ", s, "strings are ", str_j, " ", str_s)
            if j == s:
                count=count +1
                # print ("count is ", count)
    return count

def j_and_s_2(str_j, str_s):
    count = 0
    for s in str_s:
        # print ("s is ", s, "strings are ", str_j, " ", str_s)
        if s in str_j:
            count=count +1
            # print ("count is ", count)
               
    return count


def j_and_s_3(str_j, str_s): 
    # make a set from the string
    set_j = set(str_j) 
    count = 0
    # print(set_j)
    for s in str_s:
        if s in set_j:
            count += 1
    return count








