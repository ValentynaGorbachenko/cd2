#reverse a list

def reverseList(arr):
    j = len(arr)-1
    for i in range(len(arr)//2):
        arr[i], arr[j] = arr[j], arr[i]
        j -=1
    print (arr)

reverseList([1,2,3,4,5])
