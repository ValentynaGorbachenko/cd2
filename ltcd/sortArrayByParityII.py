'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''
def sortArrayByParityII(arr):
    
    for i, elem in enumerate(arr):
        print("i and elem ",i, elem)
        if elem%2 == 0 and i%2==0:
            # all even
            continue
        elif elem%2!=0 and i%2 != 0:
            #all odd
            continue
        elif elem%2==0 and i%2 != 0:
            # even element odd index
            # pass
            j = len(arr)-1
            # while j!=len(arr)-1 and arr[j]%2!=0:
            while arr[j]%2==0 and i!=j:
                j-=1
            print(i, arr[i], j, arr[j])
            arr[i], arr[j] = arr[j], arr[i]
        elif elem%2!=0 and i%2 == 0:
            # odd element even inxed
            j = len(arr)-1
            while arr[j]%2!=0 and i!=j:
                j-=1
            print(i, arr[i], j, arr[j])
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)

sortArrayByParityII([3,5,7,9,4,6,2,8])


def asortArrayByParityII(A):
    j = 1
    for i in range(0, len(A), 2):
        if A[i] % 2:
            while A[j] % 2:
                j += 2
            A[i], A[j] = A[j], A[i]
    print(A)
    return A


def bsortArrayByParityII(A):
    res = [0] * len(A)
    odd, even = 1, 0
    for num in A:
        if num % 2:
            res[odd] = num
            odd += 2
        else:
            res[even] = num
            even += 2
    print(res)
    return res

asortArrayByParityII([3,5,7,9,4,6,2,8])
bsortArrayByParityII([3,5,7,9,4,6,2,8])

