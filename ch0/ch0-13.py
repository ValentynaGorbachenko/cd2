'''
Countdown by 4
'''
def countByFour(num):
	while num>0:
		if num%4==0:
			print num
			num-=4
		else:
			num-=1

countByFour(2016)