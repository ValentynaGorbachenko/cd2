# Values Greater Than Second
'''
For [1,3,5,7,9,13], print values that are greater than its 2nd value. 
'''
def valueGreaterThanSecond(arr):
	arrRes = []
	if (len(arr)>1 and isinstance(arr[1], int)):
		for i in arr:
			if (isinstance(i, int)):
				if (i>arr[1]):
					arrRes.append(i)
	print arrRes
valueGreaterThanSecond([])
valueGreaterThanSecond([2])
valueGreaterThanSecond([5, 2])
valueGreaterThanSecond([5, 2, 3])
valueGreaterThanSecond(["a", 2, 4, "6", 3])