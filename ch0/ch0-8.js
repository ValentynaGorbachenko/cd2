/*
Print and count
*/
function printAndCount(){
	let count =0;
	for (let i=512; i<=4096;){
		if (i%5==0){
			console.log(i);
			count++;
			i+=5;
		} else {
			i++;
		}
	}
	console.log("Count is "+count)
}
printAndCount();