'''
Fib (hacker challenge). Write a function fib() in Python that returns 
the appropriate Fibonacci number.  Do this using recursion.  Let's say 
that the first two Fibonacci numbers are 0 and 1.  Remember that 
fib(n) = fib(n-2) + fib(n-1).
'''

def fib(n):
    if n < 3:
        return 1
    return fib(n-2) + fib(n-1)

print (fib(12))

def fir_iter(n):
    i, j = 0, 1
    for x in range(0, n):
        # print('before ', i, j)
        i, j = j, j+i
        # print('after ', i, j)
        # swap
        # temp = i
        # i = j
        # j = temp + j
    return i

print(fir_iter(5))
