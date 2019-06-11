def top_ten(arr):
    if (len(arr)<=10):
        arr.sort()
        return arr
    arr.sort()
    return arr[len(arr)-10:len(arr)]

print(top_ten([3,1,3,5]))
print(top_ten([2,1,4,2,-1,3,5,9,12,12,34,23]))