// Values Greater Than Second
/*
For [1,3,5,7,9,13], print values that are greater than its 2nd value. 
*/
function valueGreaterThanSecond(arr){
	let arrRes = []
	if(arr.length >1 && typeof(arr[1]) == "number"){
		for ( let i=0; i<arr.length;i++){
			if (typeof(arr[i]) == "number"){
				if (arr[i]>arr[1]){
					arrRes.push(arr[i])
				}
			}
		}
	}
	console.log(arrRes)
}

valueGreaterThanSecond([])
valueGreaterThanSecond([2])
valueGreaterThanSecond([5, 2])
valueGreaterThanSecond([5, 2, 3])
valueGreaterThanSecond(["a", 2, 4, "6", 3])