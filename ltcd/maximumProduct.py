'''
Given an integer array, find three numbers whose product is maximum and 
output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and 
all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 
32-bit signed integer.
'''

def maximumProduct(nums):
    nums.sort()
    
    if nums[len(nums)-3]*nums[len(nums)-2]*nums[len(nums)-1] >= nums[len(nums)-len(nums)]*nums[len(nums)-len(nums)+1]*nums[len(nums)-1]:
        return nums[len(nums)-3]*nums[len(nums)-2]*nums[len(nums)-1]
    else:
        return nums[len(nums)-len(nums)]*nums[len(nums)-len(nums)+1]*nums[len(nums)-1]



print("max is ",maximumProduct([-6,-5,-1,2,3]))
print("*"*8)
print("max is ",maximumProduct([1,2,3]))
print("*"*8)
print("max is ",maximumProduct([-6,-5,1,2,3,4]))
print("*"*8)
print("max is ",maximumProduct([-6,1,2,3,4]))
