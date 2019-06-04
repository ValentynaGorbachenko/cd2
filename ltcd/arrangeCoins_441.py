'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''

def arrangeCoins2(n):
    count = 1
    while n > 0:
        print("*"*count)
        n -= count
        if n >= 0:
            count +=1   

    return count - 1

def arrangeCoins3(n):
    i = 1
    while n>=i:
        n, i = n-i, i+1
    return i-1

def arrangeCoins(n):
    print("*"*8)
    start = 0
    end = n

    while start+1<end:
        mid = start + (end-start)//2
        total = (mid+1)*mid//2
        print("mid and total ", mid, total)
        if total == n: 
            return mid
        elif total < n:
            start = mid
        else:
            end = mid
        print("start nad end ", start, end)

    if (end+1)*end//2 <= n:
        return end
    else:
        return start