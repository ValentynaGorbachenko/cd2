'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
'''

def duplicateZeros2(arr):
    z=1
    for i in range(1,len(arr)):
        if z<len(arr):
            print("z is ",z, "and arr[i-1] is ",arr[i-1])
            if arr[z-1]==0:
                j=len(arr)-1
                while j!=z:
                    arr[j]=arr[j-1]

                    j-=1
                arr[j]=0
                z+=1
                print(arr)
            z+=1

    print(arr)

def duplicateZeros(arr):
    i=1
    while i<len(arr):
        print("in while, i is ", i)
        if arr[i-1]==0:
            arr.insert(i,0)
            arr.pop()
            i+=1
        i+=1

    print(arr)


# print(duplicateZeros([1,0,2,3,0,4,5,0]))
print(duplicateZeros([1,5,2,0,6,8,0,6,0]))
# print(duplicateZeros([1,2,3]))