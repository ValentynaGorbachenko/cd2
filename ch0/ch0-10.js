/* 
Counting the Dojo Way
*/
function divisible(){
	for (var i = 1; i <=100; i++) {
		if (i%5==0 && i%10==0){
			console.log("Coding Dojo");
		} else if (i%5==0){
			console.log("Coding");
		}
		else {
			console.log(i);
		}
	};
}
divisible();

function divisible2 (){
	
	for (let i=1; i<=100; i++){
		let result = " ";
		if (i%5==0){
			result = "Coding";
			if (i%5==0 && i%10==0){
				result+=" Dojo"
			}
			console.log(result)
		}
		else {
			console.log(i)
			
		} 
	}
}
divisible2();