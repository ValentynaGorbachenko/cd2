// Countdown
/*
Create  function that accepts a number as an input. Return a new array that count down by one, 
from the number (as array's zerro's element) down to zero (as the last element). How long is this array?
*/
function countdown (num){
	let arr = new Array(0)
	for (; num>=0; num--){
		arr.push(num)
	}
	console.log(arr.length)
	console.log(arr)
}
countdown(5)