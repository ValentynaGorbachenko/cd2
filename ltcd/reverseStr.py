'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''

def reverseStr(s, k):
    temp = ""

    for x in range(0,len(s),k*2):
        print('x is ',x)
        print(s[x:(x+k)])
        # reverse string here 
        if len(s[x:(x+k)]) < k and x != 0:
            print("in if ")
            temp += s[x:(x+k)]
        # elif len(s[x:(x+k)]) < k:

        else:
            temp_arr = list(s[x:(x+k)])
            temp_arr.reverse()
            print(temp_arr)
            temp += "".join(temp_arr)
            temp += s[x+k:x+k*2]
    print(temp)
    return temp

reverseStr("abcdefghijkl",5)
reverseStr("abcdefg",8)
# reverseStr("fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39)
# "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi"

'''
"abcdefg"
2
"abcdefg"
8


"bacdfeg"
"gfedcba"

'''


