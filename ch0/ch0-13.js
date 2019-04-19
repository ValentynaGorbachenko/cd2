// Countdown by 4
/*
Log positive numbers starting at 2016, counting down by 4 (exclude 0), without For loop 
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