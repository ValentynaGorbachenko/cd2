'''
X is a good number if after rotating each digit individually by 180 degrees, 
we get a valid number that is different from X.  Each digit must be rotated - 
we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 
0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 
6 and 9 rotate to each other, and the rest of the numbers do not rotate 
to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000]
'''

def rotatedDigits(num):
    num_dict = {'2':'5','5':'2','6':'9','9':'6','0':'0', '1':'1', '8':'8'}
    num_invalid = {'3', '4', '7'}
    invalid = False
    # res=[]
    count = 0
    for n in range(1,num+1):
        invalid = False
        str_n = str(n)
        str_res_temp = ""
        for i in str_n:
            if i in num_dict:
                # print('num_dict[i] ',num_dict[i])
                str_res_temp += num_dict[i]
            else:
                invalid = True
        # print("str_res_temp ",str_res_temp)
        if not invalid: # and 
            if str(n) != str_res_temp:
                # res.append(str_res_temp)
                count+=1
    # print(res,count)
    return count

rotatedDigits(20)
rotatedDigits(857) #247






