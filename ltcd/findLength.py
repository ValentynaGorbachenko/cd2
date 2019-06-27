'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''

def findLength(A,B): # doesn't work
    count=0
    max_count=0

    for i, el in enumerate(A):
        print(i,el)
        try:
            print("in try")
            j=B.index(el)
            
            while A[i] == B[j]:
                print('A[i], B[j] is ', A[i], ", ", B[j])
                count+=1
                i+=1
                j+=1
        except:
            # continue
            # break
            pass
            # print("index out of range", )
        print('conut is ',count)
        if max_count<count:
            max_count=count
        count=0
    print("max is ", max_count)
    return max_count
# findLength([1,2,3,2,1],[3,2,1,4,7])
# findLength([0,1,1,1,1,0],[1,1,1,1])
# findLength([0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0])



def findLength2(A,B): # brute force 
    count=0
    max_count=0

    for i, el in enumerate(A):
        
        for j, el_j in enumerate(B):
            print('i is ',i, ', el is ',el, ', j is ',j, ', el_j is ', el_j)
            ii = i
            try:
                print("in try")

                while A[ii] == B[j]:
                    print('A[ii], B[j] is ', A[ii], ", ", B[j])
                    count+=1
                    ii+=1
                    j+=1
                
            except:
                
                pass
                print("index out of range")
            print('conut is ',count)
            if max_count<count:
                max_count=count
            count=0
    print("max is ", max_count)
    return max_count

# findLength2([1,2,3,2,1],[3,2,1,4,7])
# findLength2([0,1,1,1,1,0],[1,1,1,1])
# findLength2([0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0])

def findLength3(A, B):
    matrix = []
    # print(matrix)
    max_count = 0
    for i in range(len(A)):
        matrix.append([])
        for j in range(len(B)):
            
            if A[i] == B[j]:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
            
            if matrix[i][j] == 1:
                    
                if i >=1 and j >= 1:
                    matrix[i][j] += matrix[i-1][j-1]


        # print(max(max(matrix)))
        # print(((i,matrix[i], max(matrix[i]), max_count)))
        if max_count<max(matrix[i]):
            max_count = max(matrix[i])

    # print(matrix)
    # print('max_count is ',max_count)
    return max_count
# findLength3([1,2,3,2,1],[3,2,1,4])
# findLength3([0,1,1,1,1,0],[1,1,1,1])
print(findLength3([0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0]))

# from solutions
def findLength4(A,B):
'''
        Intuition and Algorithm
Since a common subarray of A and B must start at some A[i] and B[j], let dp[i][j] be the longest common prefix of A[i:] and B[j:]. Whenever A[i] == B[j], we know dp[i][j] = dp[i+1][j+1] + 1. Also, the answer is max(dp[i][j]) over all i, j.
We can perform bottom-up dynamic programming to find the answer based on this recurrence. Our loop invariant is that the answer is already calculated correctly and stored in dp for any larger i, j.
Time Complexity: O(M*N), where M, N are the lengths of A, B.
Space Complexity: O(M*N), the space used by dp.  
      
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        print(memo)
        for i in range(1,len(A)+1):
            for j in range(1, len(B)+1):
                if A[i]==A[j]:
                    memo[i][j] = memo[i-1][j-1]+1
                else:
                    memo[i][j] = memo[i-1][j-1]
        #for i in range(len(A) - 1, -1, -1):
            #for j in range(len(B) - 1, -1, -1):
                #if A[i] == B[j]:
                    #memo[i][j] = memo[i+1][j+1]+1
        print(memo)
        return max(max(row) for row in memo)'''


    def check(length):
        seen = {A[i:i+length]
            for i in range(len(A) - length + 1)}
        return any(B[j:j+length] in seen
                for j in range(len(B) - length + 1))
    A = ''.join(map(chr, A))
    B = ''.join(map(chr, B))
    lo, hi = 0, min(len(A), len(B)) + 1
    while lo < hi:
        mi = (lo + hi) // 2
        if check(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo - 1

