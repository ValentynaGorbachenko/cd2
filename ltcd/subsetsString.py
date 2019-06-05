'''
There is a dictionary already implemented. Write a method, which takes input String 
without space, to prints all subsets of the input string which is present in dictionary.

Example: Dictionary – a*
………….Input- aaabaa
………….Output- a,a,a,aa,aa,aaa,a,a,aa

'''

def subsetStringInDict(s):
    dictionary = {'a':None, 'b':None, 'c':None}
    res = []
    end = 0
    beg = 0
    for i in range(len(s)):
        
        print(i, s[i])
        if s[i] in dictionary:
            print("in if end is ", end)
            end += 1
        else:
            print("in else ",i, beg,end, s[i:end])
            temp = subsetString(s[beg:end])
            print("temp is ", temp)
            res.extend(temp)
            end = i+1
            beg = i+1
    print("out ",i, beg,end, s[i:end])
    temp = subsetString(s[beg:end])
    print("temp is ", temp)
    res.extend(temp)
    print (res)


def subsetString(s):
    res = []
    for i in range(len(s)):
        # print ("s[i] is ",s[i])
        for j in range(i+1, len(s)+1):
            # print(j, len(s)+1)
            # print(s[i:j])
            res.append(s[i:j])
    res.sort()
    return res
print(subsetString('aaa'))
subsetStringInDict('aaagaaggga') # a,a,a,aa,aa,aaa,a,a,aa
# subsetStringInDict('aaagaa')

'''
There is a dictionary already implemented. Write a method , 
which takes input String without space, to replace the characters 
from the strings which are not present in dictionary with –

Example: Dictionary – a*
………….Input- aaabaa
………….Output- aaa_aa
'''

def replaceString(s):
    dictionary = {'a':None}
    for i in range(len(s)):
        if s[i] not in dictionary:
            s = s.replace(s[i], '_')

    print (s)

# replaceString('aaabaa')