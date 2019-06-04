'''
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list 
(including duplicates).  For example, if a character occurs 3 times 
in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''

def commonChars(arr):
    if len(arr)>0:
        first_word = set(arr[0])
        # print("first_word is ", first_word)
    else:
        return arr
    res = []
    for char in first_word:
        temp = []
        for word in arr:
            # print(word, char)
            char_count = word.count(char)
            temp.append(char_count)
        # print(temp)
        min_times = min(temp)
        res.extend([char]*min_times)
    # print ("*"*20,"\nresult is ", res)
    return res


print(commonChars(["bella","label","roller"]))
print(commonChars(["cool","lock","cook"]))
print(commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]))
print(commonChars([]))
print(commonChars(["","",""]))