let sentence="The weather is not as bad as I expected"
let search_word ='not'
let search_word1 = 'bad'
words = sentence.split(" ")
let wordNot = words.indexOf(search_word.toLowerCase());
let wordBad = words.indexOf(search_word1.toLowerCase());
console.log(wordNot, wordBad)

replace_str= 'good'
if (wordBad>wordNot) {
    words.splice(wordNot, wordBad - wordNot + 1, replace_str);
}
let result= words.join(" ")
console.log(result)