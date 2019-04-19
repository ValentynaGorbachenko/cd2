# Print and count
'''
Print all inegers multipels of 5, from 512 to 4096. Afterward, also log how many there were
'''
def printAndCount():
	count = 0
	for i in range (512, 4096):
		if (i%5==0):
			print i
			count+=1
			i+=5
		else:
			i+=1
	print "Count is " + str(count)

printAndCount()