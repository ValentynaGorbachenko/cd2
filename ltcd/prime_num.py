# function that returns an array with prime number up to n
def prime_num(n):
    res = []
    for num in range(1, n+1):
        print ('num is ',num)

        if num >= 2:

            for i in range(2, num):
                print('num%i ', num,'%',i, '=',num%i)

                if (num%i)==0:
                    print('if before break ',num)
                    break

            else:
                print('else ', num)
                res.append(num)
            
    print (res)
    return res

prime_num(7)