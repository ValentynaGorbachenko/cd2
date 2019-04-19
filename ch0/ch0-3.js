// Don't Worry, Be Happy
/*
Create a beCheerful() function and console.log "good morning" within it 98 times" 
*/
let z = (x)=>{console.log(x + " Good morning")};
function beCheerful(){
	for (let x=1; x<99; x++){
		z(x);
	}
}
// or

function y (x){
	console.log(x);
}
function beCheerful2(){
	for (let x=1; x<99; x++){
		y(x + " Good morning");
	}
}
beCheerful2()
beCheerful()