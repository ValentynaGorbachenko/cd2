// First Plus Length
/*
Given an array, return the sum of the first value in the array, plus the array's length.
What happens if the array's first value in not a number, but a string( like "what?") or a boolean (like false).
*/
function firstPlusLength(arr){
	if (arr.length==0){
		console.log("Array is empty1")
		return
	}
	try{
		console.log(arr[0]+arr.length)
	}
	catch(err){
		console.log("Error " + err)
	}
}
firstPlusLength([])
firstPlusLength([1])
firstPlusLength([false])
firstPlusLength([true])
firstPlusLength(["1"])
firstPlusLength(["what?"])

function firstPlusLength2(arr){
	if (arr.length==0){
		console.log("Array is empty")
		return
	}
	// console.log(typeof(arr[0])== "number")
	if (typeof(arr[0]) == "number"){
		console.log(arr[0]+arr.length)
		return arr[0]+arr.length
	}
	else if (typeof(arr[0]) == "boolean"){
		console.log ("The value can not be added - type error")
	}	
	else if (typeof(arr[0]) == "string"){
		console.log ("The value can not be added - type error")
	}
	else {
		console.log ("Type error")
	}
}
firstPlusLength2([])
firstPlusLength2([1])
firstPlusLength2([false])
firstPlusLength2([true])
firstPlusLength2(["1"])
firstPlusLength2(["what?"])