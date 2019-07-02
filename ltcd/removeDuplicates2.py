

def removeDuplicates3(nums):
    if len(nums) == 0:
        return 0
    j = 0
    new_len = 0
    cur_rep = 0
    for i in range(1, len(nums)):
        # print("new_len = ", new_len, "\ni = " ,i, "\nnums[i] = ", nums[i])
        # print('before ',nums)
        if nums[i] != nums[new_len]:
            
            # print("in 2")
            if nums[cur_rep] == nums[cur_rep+1]:

                new_len += 1

                nums[new_len] = nums[i-1]
                new_len += 1
                nums[new_len] = nums[i]
                cur_rep = i
            else:
                new_len+=1
                nums[new_len] = nums[i]
        j = i        
        
        # print('after ',nums)
    # new_len += 1
    print(cur_rep, j)
    if new_len+1 <len(nums) and cur_rep != j:
        nums[new_len+1] = nums[j]
        new_len +=1
    print(nums)
    return new_len + 1


# print(removeDuplicates3([0,0,0,0,1,1,2,2,2,3,4,5,6]))
print(removeDuplicates3([0,0,1,1,1,1,2,3,3]))
print(removeDuplicates3([1,2]))
print(removeDuplicates3([3]))
print(removeDuplicates3([0,0,1,1,1,1,2,3,3]))
print(removeDuplicates3([1,1,1,2,2,3]))
print(removeDuplicates3([1,2,2,3]))

