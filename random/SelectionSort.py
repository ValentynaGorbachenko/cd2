# selection sort

def sortSS(arr):
    # check if array has more than 2 values to sort
    if (len(arr)<=1):
        return arr
    
    
    # min_pos = 0
    # looping through array 
    for j in range(len(arr)-1):
        # print("j is ", j)
        min_val = arr[j]
        # print("min is ", min_val)
        for i in range(j+1, len(arr)):
            # print("i is ", i)
            # find min in the current iteration 
            if (arr[i]<min_val):
                min_val = arr[i]
                # print(arr)
                # print(min_val)
                arr[j], arr[i] = arr[i], arr[j]
                # print(arr)
    return arr


