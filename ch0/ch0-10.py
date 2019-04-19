# Counting the Dojo Way
'''
Print integers 1 to 100. If divisible by 5 print "Coding" instead. If by 10, also print " Dojo" 
'''
def divisible():
	for i in range(1,101):
		if(i%5==0 and i%10==0):
			print "Coding Dojo"
		elif (i%5==0):
			print "Coding"
		else: 
			print i

divisible()