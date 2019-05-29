# Countdown

def countdown (num):
	'''
	Create  function that accepts a number as an input. Return a new array that count down by one, 
	from the number (as array's zerro's element) down to zero (as the last element). How long is this array?
	'''
	arr = []
	for i in range (num, -1, -1):
		arr.append(i)
	print (len(arr))
	print (arr)

countdown(5)