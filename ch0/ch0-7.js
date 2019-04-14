/*
Leap Year
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