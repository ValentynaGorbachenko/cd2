'''
Flexible Countdown
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