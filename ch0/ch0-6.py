# You say it's your birthday
'''
If two given numbers represent your birth month and day in either order, 
log "Hoe did you know?", else "Just another day"
'''
def yourBirthday (x,y):
	if ((x==3 and y==8) or (x==8 and y==3)):
		print "How did you know?"
	else:
		print "Just another day"

yourBirthday(3,8)
yourBirthday(8,3)
yourBirthday(1,3)