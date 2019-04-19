# Countdown by 4
'''
Log positive numbers starting at 2016, counting down by 4 (exclude 0), without For loop 
'''
def countByFour(num):
	while num>0:
		if num%4==0:
			print num
			num-=4
		else:
			num-=1

countByFour(2016)