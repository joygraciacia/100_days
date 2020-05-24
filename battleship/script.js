var bomb;
const ship_1 = document.getElementById("s1");
const ship_2 = document.getElementById("s2");
const ship_3 = document.getElementById("s3");
const ship_4 = document.getElementById("s4");
const ship_5 = document.getElementById("s5");
var total = document.getElementById("total");


function counting(){
	console.log(counter++);
}

function main(){
	ship_1.addEventListener('click', function(){
		increment(0);
	})
	ship_2.addEventListener('click', function(){
		increment(1);		
	})
	ship_3.addEventListener('click', function(){
		increment(2);
	})
	ship_4.addEventListener('click', function(){
		increment(3);	
	})
	ship_5.addEventListener('click', function(){
		increment(4);
	})
}

function increment(input){
	total.innerHTML++;
	console.log(total.innerHTML);
	bomb = Math.floor(Math.random()*4);
	console.log(bomb);
	console.log(input);
	if(input==bomb){
		hits.innerHTML++;
	}
}

main();