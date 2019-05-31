'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
'''
def repeatedNTimes(arr):

    map_arr = {}
    n = len(arr)/2
    for i in arr:
        if i in map_arr:
            map_arr[i] = map_arr[i] + 1
        else:
            map_arr[i] = 1
    for key, value in map_arr.items():
        if value == n:
            return key

# print(repeatedNTimes([1,2,2,3]))
# print(repeatedNTimes([1,2,3,3]))
# print(repeatedNTimes([5,1,5,2,5,3,5,4]))
# print(repeatedNTimes([]))