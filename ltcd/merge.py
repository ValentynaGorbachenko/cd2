'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

def merge(nums1,m, nums2,n):
    i, j = 0, 0
    while n>0 and m>0:
        if nums1[i]>nums2[j]:
            nums1.insert(i,nums2[j])
            nums1.pop()
            j+=1
            n-=1
            m+=1
        i+=1
        m-=1
    while n>0:
        nums1[i] = nums2[j]
        i+=1
        j+=1
        n-=1

    print(nums1)

        

merge([1,2,3,0,0,0],3,[2,5,6],3)
