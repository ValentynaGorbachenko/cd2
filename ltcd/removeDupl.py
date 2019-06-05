'''
Write a program to remove duplicates from array of prime numbers.
'''

def removeDupl1(arr):
    s = set(arr)
    print(s)
    return(list(s))



def removeDupl(arr):
    if len(arr)<2:
        return arr

    arr.sort() # n log n
    print(arr)
    temp = []
    j = 0
    for i in range(len(arr)-1):
        print(i)
        if arr[i] != arr[i+1]:
            temp.append(arr[i])
            j += 1
        print (temp, arr, j)
    temp.append(arr[len(arr)-1])
    print (temp)

removeDupl([7,7,3,5,3,2,7,7,9])