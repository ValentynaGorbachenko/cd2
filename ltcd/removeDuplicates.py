'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''

def removeDuplicates(nums):
    j=0
    for i in range(len(nums)-1):    
        i+=j
        # print(i, nums[i])
        if nums[i] == nums[i+1]:
            nums.pop(i)
            j-=1
    print(nums)
    return (len(nums))

# print(removeDuplicates([0,0,1,1,2,2,2,3,4,4]))


def removeDuplicates2(nums):
    new_len = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[new_len]:
            new_len += 1
            nums[new_len] = nums[i]

    return new_len + 1


print(removeDuplicates2([0,0,1,1,2,2,2,3,4,4]))

