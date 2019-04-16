/*
Flexible Countdown
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