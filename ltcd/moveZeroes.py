'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

def moveZeroes(nums):
    cnt = nums.count(0)
    nums.extend([0]*cnt)
    print(nums)
    j=0
    for i in range(len(nums)-cnt):
        
        i+=j
        print(i, nums[i])
        if nums[i] == 0:
            nums.pop(i)
            j-=1
        

    # while i < len(nums):
    #     print(i)
    #     if nums[i] == 0:
    #         nums.append(0)
    #         # nums.pop(i)
    #         # i -= 1

    #     i+=1

    print(nums)

moveZeroes([0,0,0,0,1,0,3,12])

