// The Final Countdown
/*
This is based on flexible countdown. Given 4 parameters param1, param2, param3, param4.
Print the multiples of param1, starting at param2 and extending to param3. One excepion: 
if multiple is equal to param4, then skip that one (don't print). Do this usinf While.
Given 3,5,17,9, print 6,12,15
*/
function finalCount(p1,p2,p3,p4){
	if (p2>p3 || p1==0){
		console.log("Error")
		return
	}
	for (;p2<=p3;){
		if(p2%p1==0 && p2!=p4){
			console.log(p2)
			p2+=p1
		} else {
			if (p2==p4){
				p2+=p1
			} else {
				p2++
			}
			
		}
	}
}
finalCount(3,5,17,9)
finalCount(3,50,17,9)
finalCount(0,5,17,9)
finalCount(0,50,17,9)
finalCount(3,5,17,12)