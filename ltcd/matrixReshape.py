'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''

def matrixReshape(nums, r, c):
    # get a number of elements in current matrix
    try:
        nums_of_elements = len(nums)*len(nums[0])
    except IndexError:
        nums_of_elements = 0

    print(nums_of_elements, r*c)
    # check if reshape is possible
    if nums_of_elements != r*c:
        return nums

    temp = []
    res = [[0]*c]*r
    rr=[]
    print(res, r, c)
    # flatten a matrix
    for x in nums:
        temp.extend(x)

    print(temp)
    
    count = 0
    for i in range(r):
        print(i)
        
        rr.append([])

        for j in range(c):
            rr[i].append(temp[count])
            count+=1
            
        # for j in range(c):
        #     res[i][j] = temp[count]
        #     count+=1
    print(rr)
    return rr

# matrixReshape( [[1,2],[3,4]] , 4,1)

def matrixReshape2(nums, r, c):
    rows = len(nums)
    cols = len(nums[0])
    
    if rows*cols == r*c:
        numsI = [x for y in nums for x in y]
        numsR = [numsI[i:i+c] for i in range(0, len(numsI), c)]
    else:
        return nums
        
    return numsR
print(matrixReshape2( [[1,2],[3,4]] , 4,2))