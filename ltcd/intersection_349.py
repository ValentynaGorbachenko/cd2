'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

def intersect(nums1, nums2):
    res = []
    if len(nums1)<len(nums2):
        set_num = set(nums1)
        working_arr = nums2
    else:
        set_num = set(nums2)
        working_arr = nums1
        
    for key in set_num:
        if int(key) in working_arr:
            res.append(int(key))

    return res