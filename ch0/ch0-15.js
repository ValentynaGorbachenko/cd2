/*
The Final Countdown
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