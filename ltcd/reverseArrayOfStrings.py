# reverseArrayOfStrings.py

def reverseArrayOfStrings(arr):
    # initialization, pointer is for another implementation
    rev_str, res, beg, end, pointer = "", [], 0, 0, 0
    # print (rev_str, res,beg, end)

    # traverse through array from the end 
    for i in range(len(arr)-1, -1, -1):
        print (arr[i])
        # traverse through the item from the end and create reverse string
        for j in range(len(arr[i])-1, -1, -1):
            print(arr[i][j])
            # at this point I can try to use pointer to start adding to result array
            rev_str += arr[i][j]

    print (rev_str)

    # traverse through array from begining to end
    for item in arr:
        # find length of the first word, slice the string, add to result array
        end += len(item)
        res.append(rev_str[beg:end])
        beg = end

    print(res)

def reverseArrayOfStrings2(arr):
    # initialization, pointer is for another implementation
    rev_str, res, pointer, temp = "", [], 0, ""
    # print (rev_str, res,beg, end)

    # traverse through array from the end 
    for i in range(len(arr)-1, -1, -1):
        print (arr[i])
        # traverse through the item from the end and create reverse string
        for j in range(len(arr[i])-1, -1, -1):
            print(arr[i][j])
            temp += arr[i][j]

            # check if length of temp is equal to the length of array element
            if len(temp) == len(arr[pointer]):
                res.append(temp)
                pointer += 1
                temp = ""
    print (res)
    return res


reverseArrayOfStrings2(["I", "like", "big", "butts!"])
reverseArrayOfStrings(["I", "like", "big", "butts!"])