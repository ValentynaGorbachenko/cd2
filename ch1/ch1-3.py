# First Plus Length
'''
Given an array, return the sum of the first value in the array, plus the array's length.
What happens if the array's first value in not a number, but a string( like "what?") or a boolean (like false).
'''
def firstPlusLength(arr):
	try:
		print arr[0]+len(arr)
	except:
		print "Error"

firstPlusLength([])
firstPlusLength([1])
firstPlusLength([False])
firstPlusLength([True])
firstPlusLength(["1"])

def firstPlusLength2(arr):
	if (len(arr)==0):
		print "Array is empty"
		return
	if (isinstance(arr[0], bool)):
		print "The value can not be added - type error"
	elif (isinstance(arr[0], str)):
		print "The value can not be added - type error"
	elif isinstance(arr[0], int):
		print arr[0]+len(arr)
		return arr[0]+len(arr)
	else:
		print "Type error"

firstPlusLength2([])
firstPlusLength2([1])
firstPlusLength2([False])
firstPlusLength2([True])
firstPlusLength2(["1"])
firstPlusLength2(["what?"])
