# Leap Year
'''
Write a function that determines whether a given year is a leap year. 
If a year is divisible by four, it is a leap year, unless it is divisible by 100. 
However, if it is divisible by 400, then it is.
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