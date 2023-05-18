let i=prompt("How many bottles?");
let i_num=Number(i)

console.log(i_num + ' bottles of beer on the wall')
console.log(i_num +' bottles of beer')
console.log('Take 1 down, pass it around')
console.log(i_num-1 + " bottles of beer on the wall")
console.log("");
i_num=i_num-1
 
for (let bottles=2; bottles<=i_num; bottles++) {
     console.log((i_num) + ' bottles of beer on the wall');
    console.log((i_num) + ' bottles of beer');
    console.log('Take '+ (bottles)+' down, pass them around');
    console.log((i_num-bottles) + " bottles of beer on the wall");
    console.log("");
    i_num=i_num-bottles;
}
