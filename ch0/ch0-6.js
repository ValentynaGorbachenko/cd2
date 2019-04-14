/* 
You say it's your birthday
*/
function yourBirthday (x, y) {
	if ((x==3 && y==8) || (x==8 && y==3)){
		console.log("How did you know?");
	} else {
		console.log("Just enother day");
	}
}
yourBirthday(8,3);
yourBirthday(3,8);
yourBirthday(8,1);