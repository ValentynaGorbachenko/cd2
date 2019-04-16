'''
Whoa, that sucker's huge
'''
def oddSum(beg, end):
	sum=0
	if beg > end:
		print "Error"
	if beg+end==0:
		print sum
	else:
		for i in range(beg, end+1):
			if i%2==1:
				sum+=i
				print sum
		# print sum

oddSum(10,27)