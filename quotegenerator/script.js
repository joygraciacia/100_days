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

function randomNumber(){
  return Math.floor(Math.random()*Object.keys(quotes).length);
}


function newQuote(){
  /*
  var randomNumber = Math.floor(Math.random()*Object.keys(quotes).length);
  */
  /*
  document.getElementById('quotedisplay').innerHTML = Object.values(quotes)[3];
  */

  $quotedisplay = Object.values(quotes)[3];

  console.log(Object.values(quotes)[5]);
}

/* short cut to document.getElementById
var $button = document.querySelector('.button');
*/

function answer(){


}
