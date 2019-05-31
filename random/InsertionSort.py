# insertinon sort

def sortIS(arr):
	# check if array has more than 2 values to sort
	if (len(arr)<=1):
		return arr
	
	# main logic - srart from the second element
	for i in range(1,len(arr)):
		
		# check if previous value is smaller 
		if (arr[i]<arr[i-1]):
			
			# assign two new locators for moving values
			j=i-1
			z=i
			
			# move smaller value up until it on its right position
			while (arr[z]<arr[j]):
				arr[z], arr[j] = arr[j], arr[z]
				
				# update two locators
				j=j-1
				z=z-1
				
				# check if we are in the range of array
				if (j == -1):
					break
	return arr

