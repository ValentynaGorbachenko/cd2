'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you 
cannot load all elements into the memory at once?

'''

def make_a_dict(arr):
    temp = {}
    for i in range(len(arr)):
        if str(arr[i]) not in temp:
            temp[str(arr[i])] = 1
            # print("if ",temp)
        elif str(arr[i]) in temp:
            temp[str(arr[i])] += 1
            # print("elif ",temp)
    return temp

def intersect(nums1, nums2):
    res = []
    if len(nums1)<len(nums2):
        dict_num = make_a_dict(nums1)
        working_arr = nums2
    else:
        dict_num = make_a_dict(nums2)
        working_arr = nums1
    print (dict_num)
    for key, value in dict_num.items():
        print("key is ",key,"value is ", value)
        print(working_arr)
        print (working_arr.count(int(key)))
        rep = working_arr.count(int(key))
        res.extend([int(key)]*(min(rep, value)))
    print (res)

    return res