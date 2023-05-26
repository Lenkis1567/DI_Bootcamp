// first version


// let string1=prompt ('Input the first string')
// let string2=prompt ('Input the second string')


// removeSpaces = str => str.split(' ').join('');

// function compareAn (str1, str2){
// let str1R=removeSpaces(str1);
// let str2R=removeSpaces(str2);
// const length1=str1R.length;
// const length2=str2R.length;
// if (length1!==length2){console.log ('not anagrams')}
// else {
//     for (let i=0; i<length1; i++) {
//         if (str1R[i] !== str2R[length1-1-i]) {
//             console.log ('not anagrams');
// break
//         } 
//       console.log ('anagrams')  
//     }
// }
// }
// compareAn(string1, string2)

// second version

let string1 = prompt('Input the first string');
let string2 = prompt('Input the second string');

const removeSpaces = str => str.split(' ').join('');

let str1WS = removeSpaces(string1);
let str2WS = removeSpaces(string2);

const len1 = str1WS.length;
const len2 = str2WS.length;

const isAnagram = len1 === len2 && str1WS.split('').every((char, i) => char === str2WS[len1 - 1 - i]);

console.log(isAnagram ? 'anagrams' : 'not anagrams');