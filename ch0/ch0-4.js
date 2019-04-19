// Multiples of Tree but not all
/*
Using For loop print multiples of 3 from -300 to 0. Skip -3 and -6
*/
for (var i = -300; i <= 0; i+=3) {
	if (i != -3 && i != -6){
		console.log(i);
	}
};

console.log( true || true); // true
console.log( true || false); // true
console.log( false || false); // false
console.log( true && true); // true
console.log( true && false); // false
console.log( false && false); // false