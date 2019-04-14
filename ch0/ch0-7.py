'''
Leap Year
'''
def leapYear(year):
	if (year%4==0):
		if (year%100==0 and year%400==0):
			print "leap"
		elif (year%100==0):
			print "not leap"
		else:
			print "leap"
	else:
		print "not leap"

leapYear(1000)
leapYear(2000)
leapYear(2004)
leapYear(1931)