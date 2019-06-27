'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''

def isMonotonic(A):
    # if any elements 
    if len(A)>=1:
        # if one or the same elements
        # if sum(A)/len(A) == A[0]:
        #     return True

        min_el = min(A)
        pos_min = A.index(min_el)

        max_el = max(A)
        pos_max = A.index(max_el)

        print(min_el, pos_min, max_el, pos_max)

        # increasing
        if pos_min < pos_max:
            print("in increasing")
            for i in range(len(A)-1):
                print("i is ", i, " and A[i] is ", A[i], " and A[i+1] is ", A[i+1])
                if not A[i] <= A[i+1]:
                    return False

        else:
            # decreasing
            print("in decreasing")
            for i in range(len(A)-1):
                print("i is ", i, " and A[i] is ", A[i], " and A[i+1] is ", A[i+1])
                if not A[i] >= A[i+1]:
                    return False

        return True






print(isMonotonic([1,1,1])) # True
# print(isMonotonic([1,2,4,5])) # True
# print(isMonotonic([1,2,1,4,5])) # False
# print(isMonotonic([1,3,2])) # False
# print(isMonotonic([6,5,4,4])) # True
# print(isMonotonic([1,2,2,3])) # True

# print(isMonotonic([5,3,2,4,1])) # False

print(isMonotonic([3,4,2,3])) # False 

print(isMonotonic([3])) # True 




