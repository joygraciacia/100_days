const chuck_p = document.getElementById("chuck");
const blair_p = document.getElementById("blair");
const dan_p = document.getElementById("dan");
const serena_p = document.getElementById("serena");
var x; 

var quotes = {
  "dan": ["you are no one until you're talked about"],
  "blair" : ["if you're going to be sad, you might as well be sad in paris"],
  "chuck" : ["three words. eight letters. say it and i'm yours"],
  "blair" : ["you can't make people love you but you can make them fear you"],
  "blair" : ["maybe i am a total bitch. ever think about that"],
  "blair" : ["what i want, is to become a powerful woman"],
  "serena" : ["i don't need friends, i need more champagne"],
  "chuck" : ["if two people are meant to be together, eventually they'll find their way back"],
  "blair" : ["if you really want something, you don't stop for anyone or anything until you get it"]
}

function main(){
  chuck_p.addEventListener('click', function(){
    check("chuck");
  })
  blair_p.addEventListener('click', function(){
    check("blair");
  })
  dan_p.addEventListener('click', function(){
    check("dan");
  })
  serena_p.addEventListener('click', function(){
    check("serena");
  })
}

function newQuote(){
  randomNumber = Math.floor(Math.random()*Object.keys(quotes).length);
  document.getElementById('quotedisplay').innerHTML = Object.values(quotes)[randomNumber];
  x = Object.keys(quotes)[randomNumber];
  console.log(x);
  return x;
}


function check(userChoice){
  // var answer = newQuote();
  console.log(x);
  if(x==userChoice && x== "chuck"){
    console.log("chuck");
    document.getElementById('fakebutton').innerHTML = "You're right! It's Chuck";
  }else if(x==userChoice && x== "blair"){
    console.log("blair");
    document.getElementById('fakebutton').innerHTML = "You're right! It's Blair";
  }else if(x==userChoice && x== "dan"){
    console.log("dan");
    document.getElementById('fakebutton').innerHTML = "You're right! It's Dan";
  }else if(x==userChoice && x== "serena"){
    console.log("serena");
    document.getElementById('fakebutton').innerHTML = "You're right! It's Serena";
  }else{
    console.log("none")
    document.getElementById('fakebutton').innerHTML = "Try again.";
  }
}

/* short cut to document.getElementById
var $button = document.querySelector('.button');
*/
main();