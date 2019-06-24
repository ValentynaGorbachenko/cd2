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

def findLength(A,B):
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



def findLength2(A,B):
    count=0
    max_count=0

    for i, el in enumerate(A):
        # print(i,el)
        for j, el_j in enumerate(B):
            print('i is ',i, ', el is ',el, ', j is ',j, ', el_j is ', el_j)
            ii = i
            try:
                print("in try")
                # j=B.index(el)
                # # while I can find index of el try checking next index of el
                # ind = j

                while A[ii] == B[j]:
                    print('A[ii], B[j] is ', A[ii], ", ", B[j])
                    count+=1
                    ii+=1
                    j+=1
                # print ('ind is ', ind, B[ind+1:])
                # ind=B[ind+1:].index(el)
                # print ('ind is ',ind)
                
            except:
                # continue
                # break
                pass
                print("index out of range")
            print('conut is ',count)
            if max_count<count:
                max_count=count
            count=0
    print("max is ", max_count)
    return max_count

findLength2([1,2,3,2,1],[3,2,1,4,7])
findLength2([0,1,1,1,1,0],[1,1,1,1])
findLength2([0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0])



