# bubble sort

def sortBS(arr):
	# check if arr has something to sort
	if (len(arr) <= 1):
		return arr

	# going through array 
	for j in range(len(arr)-1):
		for i in range(len(arr)-1-j):
			if (arr[i]>arr[i+1]):
				print ('before', arr)
				arr[i], arr[i+1] = arr[i+1], arr[i]
				print ('after', arr)
	print ("*"*20)
	return arr