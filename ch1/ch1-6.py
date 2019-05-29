def fit_the_first_value(arr):
    """
    Your function should accept an array. If any value at [0] is greater than array's length, print "Too big!"
    If value at [0] is less than array's length print "Too smal", otherwise "Just right"
    """
    try:
        if arr[0]>len(arr):
            print ("Too big")
        elif arr[0]<len(arr):
            print ("Too small")
        else:
            print("Just right")
    except IndexError:
        print ("index error") 
    except TypeError:
        print ("type error")

print (fit_the_first_value.__doc__)
fit_the_first_value("hjj")
fit_the_first_value([])
fit_the_first_value("")
fit_the_first_value(3)
fit_the_first_value([1])
fit_the_first_value([-2])
fit_the_first_value([3,2])
