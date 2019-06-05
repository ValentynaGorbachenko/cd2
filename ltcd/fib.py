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

print (fib(5))