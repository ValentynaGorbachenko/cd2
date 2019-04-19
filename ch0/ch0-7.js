// Leap Year
/*
Write a function that determines whether a given year is a leap year. 
If a year is divisible by four, it is a leap year, unless it is divisible by 100. 
However, if it is divisible by 400, then it is.
*/
function leapYear(year){
	if (year%4==0){
		if (year%100==0 && year%400==0){
			console.log("leap")
		} else if (year%100==0){
			console.log("not leap")
		} else {
			console.log("leap")
		}
	} else {
		console.log("not leap")
	}
}
leapYear(1000)
leapYear(2000)
leapYear(2004)
leapYear(1931)