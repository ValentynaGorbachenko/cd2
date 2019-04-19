// Flexible Countdown
/*
Based on earlier "Contdown By Four", given lowNum, highNum, mult, 
print multiples of mult from highNum to lowNum, using for loop. 
For (2,9,3), print 9 6 3 (on successive lines)
*/
function countByFourFl (highNum, lowNum, mult) {
	if (highNum<lowNum || mult == 0){
		console.log("Error")
		return
	}
	while (highNum>=lowNum){
		if (highNum%mult==0){
			console.log(highNum)
			highNum-=mult
		} else {
			highNum--
		}
	}
}
countByFourFl(40,20,3)