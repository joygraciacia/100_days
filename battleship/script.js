var bomb;
const ship_1 = document.getElementById("s1");
const ship_2 = document.getElementById("s2");
const ship_3 = document.getElementById("s3");
const ship_4 = document.getElementById("s4");
const ship_5 = document.getElementById("s5");
var total = document.getElementById("total");
var mode = "easy";
const level_one = document.getElementById("one");
const level_two = document.getElementById("two");

function counting(){
	console.log(counter++);
}

function main(){
	level_one.addEventListener('click', function(){
		level("easy");		
	})
	level_two.addEventListener('click', function(){
		level("hard");		
	})

	ship_1.addEventListener('click', function(){
		increment(0, mode);
	})
	ship_2.addEventListener('click', function(){
		increment(1, mode);		
	})
	ship_3.addEventListener('click', function(){
		increment(2, mode);
	})
	ship_4.addEventListener('click', function(){
		increment(3, mode);	
	})
	ship_5.addEventListener('click', function(){
		increment(4, mode);
	})
}

function level(a){
	// console.log(mode);
	// console.log(a);
	if(a == "easy"){
		mode = "easy";
	}
	if(a == "hard"){
		mode = "hard";
	}
	// console.log(mode);
	return mode;
}
//hard
function increment(input, mode){
	console.log(mode);
	total.innerHTML++;
	if(mode == "easy"){}
		bomb = 1;
	if(mode == "hard"){
		bomb = Math.floor(Math.random()*4);
		console.log(bomb);
		console.log(input);
	}
	if(input == bomb){
		hits.innerHTML++;
	}
}

main();