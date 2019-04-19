# Flexible Countdown
'''
Based on earlier "Contdown By Four", given lowNum, highNum, mult, 
print multiples of mult from highNum to lowNum, using for loop. 
For (2,9,3), print 9 6 3 (on successive lines)
'''
def countByFourFl(highNum, lowNum, mult):
	if highNum<lowNum or mult==0:
		print "Error"
		return
	while highNum>=lowNum:
		if highNum%mult==0:
			print highNum
			highNum-=mult
		else:
			highNum-=1

countByFourFl(9,6, 0)