'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 

Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''

def compress(chars):
    print(chars)
    # if length of an array is one return an array
    if len(chars) == 1:
        print(chars)
        return chars

    # if length is greater 2 and greater 
    if len(chars) == 0:
        count = 0
    else:
        count = 1
    

    # go through the array  
    # for i in range(1, len(chars)-1):
    i = 1
    while i < len(chars):

        if chars[i] == chars[i-1]:
            count+=1
            # i+=1
        else:
            if count == 1:
                pass
            else:
                # pop count -1 times
                j = count-1
                while j!= 0:
                    # update j and i
                    chars.pop(j)
                    j-=1
                    i-=1
                count = [x for x in str(count)]
                print("count is ", count, chars, i)

                l = len(count)
                z=0
                while l>0:
                    chars.insert(i, count[z])

                    z+=1
                    l-=1
                    i+=1
                    print("in loop after insert ", chars, i)
                # i-=len(count)-1
            
            count = 1
            # i+=0
            print("after insert and if else ", chars, i)
        print(i, chars[i], count)
        i+=1

    # chars.insert(i, count)
    # for the last count
    print(i, count)
    if count == 1:
        pass
    else:
        # pop count -1 times
        j = count-1
        while j!= 0:
            # update j and i
            chars.pop(j)
            j-=1
            i-=1

        count = [x for x in str(count)]
        print("count is ", count)
        z=0
        l = len(count)
        while l>0:
            chars.insert(i, count[z])
            l-=1
            i+=1
            z+=1



    print(chars)





# compress(["a","a","b","b","c","c","c"])
print('*'*10)
# compress(["a"])
print('*'*10)
# compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print('*'*10)

def compress2(chars):
    # chars.sort()
    dict_chars = {}
    for i in set(chars):
        dict_chars[i] = chars.count(i)
    print(dict_chars)
    print(sum([len(str(x)) for x in dict_chars.values()]))
    print(len(dict_chars))

    for key, val in dict_chars.items():
        if val != 1:
            ind = chars.index(str(key))
            print(ind)
            i=ind+val-1
            #remove dups
            while i > ind:
                chars.pop(i)
                i-=1
            print(ind, i, chars)
            #insert count
            count = [x for x in str(val)]
            length = len(count)
            for i in range(length):
                chars.insert(ind+1+i, count[i])

        print(chars)
    return len(chars)




# compress2(["a","a","b","b","c","c","c"])
print('*'*10)
# compress2(["a"])
print('*'*10)
# compress2(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print('*'*10)
# print(compress2(["w","w","w","w","w","b","b","g","g","g","g","a","a","a","i","i","i","i","y","y","p","v","v","v","u","u","u","y","y","y","y","y","y","y","y","y","s","q","q","q","q","q","q","q","q","q","q","n","n","n"]))

print('*'*10)
print(compress2(["a","b","c","d","e","f","g","g","g","g","g","g","g","g","g","g","g","g","a","b","c"]))




