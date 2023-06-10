const { log } = require('console');
const fs = require('fs');
data=fs.readFileSync('RightLeft.txt', 'utf-8')


function countOccurrences(text, char) {
    const regex = new RegExp(char, 'g');
    const matches = text.match(regex);
    return matches ? matches.length : 0;
  }
let right = countOccurrences(data, ">");

let left = countOccurrences(data, "<");
let result = right-left

if (result > 0) {
    console.log(`${result} steps to the right`);
  } else if (result < 0) {
    console.log(`${result} steps to the left`);
  } else {
    console.log('Stay at the place');
  }


function stepsCalc(data) {
    let steps = 0;
    let i = 0;
    let res = 0;
    while (res !== -1) {
        if (data[i] === ">") {
        res=res+1
    } else {
        res = res - 1;
    }
        steps++;
        i=i+1
        } 
        return steps
    }
console.log(stepsCalc(data))

