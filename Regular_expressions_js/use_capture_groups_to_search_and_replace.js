// Use Capture Groups to Search and Replace

let wrongText = "The sky is silver.";
let silverRegex = /silver/;
console.log(wrongText.replace(silverRegex, 'blue'));

let codeCamp = 'Code Camp';
console.log(codeCamp.replace(/(\w+)\s(\w+)/, '$2 $1'));

let str = "one two three";
let fixRegex = /(\w+)\s(\w+)\s(\w+)/; // Change this line
let replaceText = "$3 $2 $1"; // Change this line
let result = str.replace(fixRegex, replaceText);

let hello = "   Hello, World!  ";
let wsRegex = /^\s*([a-zA-Z,]+)\s*([a-zA-Z!]+)\s*$/; // Change this line
result = hello.replace(wsRegex, '$1 $2');
console.log('Hello world value is:', result);