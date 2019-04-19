# The Final Countdown
'''
This is based on flexible countdown. Given 4 parameters param1, param2, param3, param4.
Print the multiples of param1, starting at param2 and extending to param3. One excepion: 
if multiple is equal to param4, then skip that one (don't print). Do this usinf While.
Given 3,5,17,9, print 6,12,15
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
