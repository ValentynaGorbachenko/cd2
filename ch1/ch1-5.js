// This Length, That Value
/*
Given two numbers, return array of legth num1, with each value num2. Print "Jinx!" if they are same.
*/
function thisLengthThatValue(num1, num2){
	try{
		var arr = new Array(num1)
	}
	catch(err) {
		console.log("error " +err)
		return
	}
	if (num1==num2){
		console.log("Jinx!")
	}
	for (let i=0; i<arr.length; i++){
		arr[i]=num2
	}
	console.log(arr)
}
thisLengthThatValue(4, 4)
thisLengthThatValue(1, 4)
thisLengthThatValue(0, 4)
thisLengthThatValue(-1, 4)