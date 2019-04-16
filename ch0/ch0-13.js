/*
Countdown by 4
*/
function countByFour (num) {
	if (num<=0){
		console.log("error")
	}
	while (num>0){
		if (num%4==0){
			console.log(num)
			num-=4
		} else {
			num--
		}
	}
}
countByFour(2016)