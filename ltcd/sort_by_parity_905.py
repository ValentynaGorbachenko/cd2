'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

'''

def sortArrayByParity(A):
    arr_even = []
    arr_odd = []
    # print(A)
    for i in A:
        if(i%2==0):
            arr_even.append(i)
        else:
            arr_odd.append(i)
    # print(arr_odd, arr_even) 
    arr_even.sort()
    arr_odd.sort()
    A = arr_even+arr_odd
    # print (A)
    return A

# print(sortArrayByParity([4,1,3,2]))
# print(sortArrayByParity([5,6,2,8,1,9]))

def even_odd(A):
    next_even , next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[ next_even ] % 2 == 0:
            next_even += 1
        else:
            A[ next_even ], A[next_odd] = A[next_odd], A[ next_even ]
            next_odd -= 1
    print (A)
s = [5,4,1,3,2]
even_odd(s)
print (s)

