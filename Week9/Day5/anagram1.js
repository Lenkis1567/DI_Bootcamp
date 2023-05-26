let string1 = prompt('Input the first string');
let string2 = prompt('Input the second string');

const removeSpaces = str => str.split(' ').join('');

// function isAnagram(str1,str2) {
//     let str1WS = removeSpaces(str1);
//     let str2WS = removeSpaces(str2);
//     const len1 = str1WS.length;
//     const len2 = str2WS.length;
//     if (len1!==len2){
//         //console.log ('not anagrams')//; 
//         return isA=false;
// }
//         else {
//             isA=true;
//             for (let i = 0; i <len1; i++) {
//                 if (str2WS.includes(str1WS[i])){
//                 str2WS=str2WS.replace(str1WS[i], '');
//                         }
//                 else {
//                     // console.log('not anagrams');
//                     isA=false;
//                 break;
//                     }; 
//                 }
//          } return isA
// }


//           SECOND VERSION

let isAnagram = (str1, str2) => {
    let str1WS = removeSpaces(str1);
    let str2WS = removeSpaces(str2);
    if (str1WS.length !== str2WS.length) {
      return false;
    }
    for (let char of str1WS) {
      if (!str2WS.includes(char)) {
        return false;
      }
      str2WS = str2WS.replace(char, '');
    }
    return true;
  }

console.log(isAnagram(string1, string2))