'''find an element in an sorted array using BS'''
def findElem(arr, value):
    if len(arr)<1 or (value < arr[0] or value > arr[(len(arr)-1)]):
        return None # or -1
    
    beg = 0
    end = len(arr)-1
    print ('beg, end is', beg, end)

    while(beg<=end):
        mid = (beg + (end - beg)//2)
        print('mid is ', mid, value)

        if value == arr[mid]:
            return mid
        elif value > arr[mid]:# and value <= arr[end]:
            print('right', beg, end)
            if arr[end] == value:
                return end
            else:
                return mid + 1 + findElem(arr[mid+1:end+1], value)

        elif value < arr[mid]:# and value >= arr[beg]:
            print('left')
            if arr[beg] == value:
                return beg
            else:
                return findElem(arr[beg:mid], value)
        
print(findElem([3,4,5,6,7,8], 4))



