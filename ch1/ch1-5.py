# This Length, That Value
'''
Given two numbers, return array of legth num1, with each value num2. Print "Jinx!" if they are same.
'''
def thisLengthThatValue(num1, num2):
	arr = []
	if (num1==num2):
		print ("Jinx!")
	for i in range(num1):
		arr.append(num2)
	print (arr)


thisLengthThatValue(4, 4)
thisLengthThatValue(1, 4)
thisLengthThatValue(0, 4)