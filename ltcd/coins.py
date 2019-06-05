'''
coins - Write a function that determines how many quarters, dimes, nickels, 
and pennies to give to a customer for a change where you minimize the number 
of coins you give out.  For example, if you need to give the customer 87 cents, 
you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  If you need to give the 
customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  
Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should 
return [3,1,1,2].
'''
def coins(num):
    if num<1:
        return []
    d = {'25':0, '10':0, '5':0, '1':0}
    res = []

    while num>0:
        if num>=25:
            d['25'] = (num//25)
            num = num - 25*(num//25)

        elif num>=10:
            d['10'] = (num//10)
            num = num - 10*(num//10)

        elif num>=5:
            d['5'] = (num//5)
            num = num - 5*(num//5)

        else:
            d['1'] = num
            num = 0

    for value in d.values():
        res.append(value)
    
    return res

print(coins(92))
print(coins(32))
print(coins(3))
print(coins(7))
print(coins(27))

        