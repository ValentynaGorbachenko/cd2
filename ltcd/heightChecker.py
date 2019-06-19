def heightChecker(arr):
    if len(arr) <=1:
        return 0

    sorted_array = list(arr)
    sorted_array.sort()
    
    count = 0
    for i in range(len(arr)):
        if arr[i] != sorted_array[i]:
            count += 1

    return count