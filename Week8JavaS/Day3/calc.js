var windowElements = document.getElementsByClassName('window')
var windowElement = windowElements[0]
let number_tocalc = ''
let number_tocalc_n=[]

function number(value) {
    let windowElements = document.getElementsByClassName('window');
    let windowElement = windowElements[0];
    let n = value;
    windowElement.textContent = windowElement.textContent+n;
    number_tocalc=number_tocalc+n;
    console.log(number_tocalc)
    return  n;
      }
console.log(number_tocalc_n);

function operator(symbol) {
var windowElements = document.getElementsByClassName('window');
var windowElement = windowElements[0];
  console.log("Clicked operator:", symbol);
  windowElement.textContent='';
  number_tocalc_n.push(number_tocalc)
  number_tocalc_n.push(symbol)
  number_tocalc = ''

}
function equal(){
    windowElement.textContent='';
    number_tocalc_n.push(number_tocalc) 
    let total = number_tocalc_n.join("")
      console.log(eval(total))
      windowElement.textContent=eval(total)
      number_tocalc_n=[]
      number_tocalc=0
      
}

