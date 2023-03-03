// Rewriting lab-2-2-1-Q1.py to JavaScript
const qLetter = "Q";

var word = prompt(`Please enter a word that starts with "${qLetter}": `)
let result = word.startsWith(qLetter) // Returns true if word starts with qLetter

alert(`It is ${result} that ${word} starts with upper case ${qLetter}.`)