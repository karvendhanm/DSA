let str_ = "Hello from Universe";
let pattern = /from/;
console.log(pattern.test(str_));

// Match literal strings
let testStr = "Hello, my name is Kevin";
let pattern1 = /kEvin/i;
console.log(pattern1.test(testStr));

// Match a literal string with different possibilities
let petString = "James has a pet cat.";
let petRegex = /dog|cat|bird|fish/; // Change this line
let result = petRegex.test(petString);
console.log('james', result);

// Ignore case while matching
let testStr1 = "Hello, my name is Kevin";
let pattern2 = /kEvin/i;
console.log(pattern2.test(testStr1));

console.log('Hello World'.match(/Hello/));
let ourStr = "Regular expressions";
let our_pattern = /expressions/;
mat = ourStr.match(our_pattern);
console.log(mat);

let extractStr = "Extract the word 'coding' from this string.";
let codingRegex = /coding/; // Change this line
let result2 = extractStr.match(codingRegex); // Change this line
console.log('result2', result2);


