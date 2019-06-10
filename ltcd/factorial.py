'''
Factorial (hacker challenge).  Write a function factorial() that returns the 
factorial of the given number.  For example, factorial(5) should return 120.  
Do this using recursion; remember that factorial(n) = n * factorial(n-1).
'''
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2

    return n*factorial(n-1)

print(factorial(5))

def factorial_iter(n):
    res = 1
    for i in range(1, n+1):
        print('before ', res, i)
        res *= i
        print('after ', res, i)

    return res
print(factorial_iter(5))