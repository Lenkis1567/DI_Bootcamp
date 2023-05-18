function isDivisible(b) {
    let arr_num = [];
   
    for (let i=1; i<500; i++) {
        if (i % b===0) {arr_num.push(i); 

        } 
    }
    return arr_num
}
function issum(arr) {
        arr_sum=0;
      for (let i=1; i<arr.length; i++) {
        var arr_sum=arr_sum+arr[i]; console.log(i, arr_sum)
        } 
   
    return arr_sum }

let b = Number(prompt("Input a number"))
let c= isDivisible(b)
summ = issum(c)
console.log(c, "The sum is ", summ)

=====================================================
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

shoppinglist=["banana", "orange", "apple"]

function myBill() {
    let price=0
    for (let i of shoppinglist){
      if (stock[i]>0) {
        price=price+prices[i];
        stock[i]=stock[i]-1
        console.log("Total quantity of", i, " is", stock[i]);
        }   
        
    }console.log("Total price is ", price) 
    }
myBill()
=============================================== What’s in my wallet==


function changeEnough(itemPrice, amountOfChange){
    console.log('You have', (0.25*amountOfChange['quarters'])+0.10*amountOfChange['dimes']+
    0.05**amountOfChange['nickel']+0.01**amountOfChange['penny'], " in your wallet, so the possubuluty to buy is ");
    return((0.25*amountOfChange['quarters'])+0.10*amountOfChange['dimes']+
    0.05**amountOfChange['nickel']+0.01**amountOfChange['penny'])>itemPrice;

}
itemPrice=Number(prompt("Input a price"))
quarters=Number(prompt("Input a quantity of quarters"));
dimes= Number(prompt("Input a quantity of dimes"));
nickel=Number(prompt("Input a quantity of nickel"));
penny = Number(prompt("Input a quantity of pennies"));
amountOfChange = {'quarters': quarters,
'dimes': dimes,
'nickel': nickel,
'penny': penny
}
console.log(changeEnough(itemPrice, amountOfChange))
====================================================Exercise 4 : Vacations Costs==============
function pricecheck() {
do{    
nights=Number(prompt('How many nights you wanna stay?'));
}
while
  (!(!isNaN(nights) && nights !== null && nights !== 0 && nights !== "" && nights > 0) )
return nights
}
function hotelCost() {
  price=pricecheck()*140;  
  console.log(price)
}
// hotelCost()


function dayscheck() {
do{    
days=Number(prompt('For how many days you wanna rent a car?'));
    }
while
    (!(!isNaN(days) && days !== null && days !== 0 && days !== "" && days > 0) )
return days
    }

function rentalCarCost(){
    days=dayscheck()
    if (days<=10){
        price=days*40;}
    else{
        price=days*40*0.95;
    }
        console.log(price)}
// rentalCarCost()

function countrycheck() {
do{ 
country=prompt('Where would you like to fly?');
}
while 
(!(isNaN(country) && country !== null && country !== 0 && country !== "" ) )
return country
}
city=countrycheck()
function planeRideCost(city){
    if (city=="London") { 
        var staying=183
    }
    else if (city=="Paris")  {
        staying=220
    }  
    else {staying=300}
    return staying
    }

// console.log(planeRideCost(city))

function totalVacationCost() {
    console.log('The car price ');
    rentalCarCost();
    console.log('The hotel price ');
    hotelCost();
    console.log('The plane cost is:', planeRideCost())
}
totalVacationCost()
==============================================================Users=============
