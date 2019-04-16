/*
Whoa, that sucker's huge
*/
function addOdd(beg, end){
	let sum = 0;
	if (beg>end){
		console.log("error")
	}
	if (beg+end==0){
		console.log(sum)
		return sum
	}
	for (;beg<=end;){
		if(beg%2==1){
			sum+=beg
			beg+=2
		} else {
			beg++
		}
	}
	console.log(sum)
}
addOdd(4,10)