'''
The Final Countdown
'''
def finalCount(p1,p2,p3,p4):
	if(p2>p3 or p1==0):
		print "Error"
		return
	for i in range(p2, p3+1):
		if (i%p1==0 and i!=p4):
			print i

finalCount(3,5,17,9)
finalCount(3,50,17,9)
finalCount(0,5,17,9)
finalCount(0,50,17,9)
finalCount(3,5,17,12)
