'''
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

 

Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length
'''

def sumEvenAfterQueries(arr, queries):
    if len(arr) != len(queries):
        return -1
    res = []
    for i, q in enumerate(queries):
        # print(i, q)
        arr[q[1]] += q[0]
        # print(arr)
        temp_count = 0

        for el in arr:
            if el%2 == 0:
                temp_count +=el

        res.append(temp_count)
        # print(res, arr)
    # print(res)
    return res


def sumEvenAfterQueries2(arr, queries):
    res = []
    sum_even = 0
    sum_even_arr =[x for x in arr if x%2==0] #returns an array

    sum_even = sum(x for x in arr if x%2==0) 
    # for el in arr:
    #     if el%2==0:
    #         sum_even+=el
    print (sum_even)

    for val, index in queries:
        if arr[index] %2 == 0:
            sum_even -= arr[index]

        arr[index] += val

        if arr[index] %2 == 0:
            sum_even += arr[index]
        
        res.append(sum_even)
    print (res)
    return res 

sumEvenAfterQueries([1,2,3,4], [[1,0], [-3,1],[-4,0],[2,3]])
sumEvenAfterQueries2([1,2,3,4], [[1,0], [-3,1],[-4,0],[2,3]])