'''find an element in an sorted array using BST'''
def findElem(arr, value):
    if len(arr)<1 or (value < arr[0] or value > arr[(len(arr)-1)]):
        return None
    mid = len(arr)//2
    beg = 0
    end = len(arr)-1
    print ('mid, beg, end is', mid, beg, end)
    while(beg<end):
        if value == arr[mid]:
            return mid
        elif value > arr[mid] and value <= arr[end]:
            if arr[end] == value:
                return end
            else:
                return findElem(arr[mid+1:end], value)

        elif value < arr[mid] and value >= arr[beg]:
            if arr[beg] == value:
                return beg
            else:
                return findElem(arr[beg:mid], value)
        
print(findElem([3,4,5,6,7,8], 9))



