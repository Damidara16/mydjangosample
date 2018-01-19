
document.getElementById('demo').innerHTML = "red car";
document.getElementById("demoo").innerHTML = 5 + 6;
var d = new Date();
var day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Firday", "Saturday"]
var dayNum = day[d.getDay()]
document.getElementById("date").innerHTML = dayNum;

var text;
function myFunc(){
    alert("Last time I checked your ass was in class")
}
switch(dayNum){
  case "Sunday":
    text = "Sleep in sleeply head";
    break;
  case "Saturday":
  text = "got an open weekend, my friend";
    break;
  case "Firday":
    text = "Walk home, you got an open weekend";
    break;
  default:
    //myFunc();
    text = '';
}
document.getElementById("dateQuote").innerHTML = text

/*
BROKEN CODE
function Person(fName, lName, age){
  this.firstName = fName
  this.lastName = lName
  this.age = age
}
//FINISH THE CONSTRUCTOR AND INCORPATE INTO THE BUTTON FUNCTION
myDad = new Person("Jack", "Fin", 31)
function nameFunc(){
  var age = document.getElementById("age");
  var fname = document.getElementById("fname");
  var lname = document.getElementById("lname");
  var name = fname + " " + lname
  var f = document.createElement('h1');
  //var k = document.createTextNode('fname');
  //f.appendChild(k);
  f.id = 'kop';
  document.getElementById('kop').innerHTML = djoo;
  document.body.appendChild(f);
}*/
