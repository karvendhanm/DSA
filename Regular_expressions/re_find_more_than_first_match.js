let testStr = 'Repeat, Repeat, Repeat';
let pattern = /Repeat/;
let res = testStr.match(pattern);
console.log(res);

// For findall use the g flag.
let pattern1 = /Repeat/g;
let res_find_all = testStr.match(pattern1);
console.log(res_find_all);

let testStr2 = 'Repeat, repeat, RePeat';
let pattern2 = /Repeat/gi;
let res2 = testStr2.match(pattern2);
console.log('two flags put together', res2);

// single character wild cards
let exampleStr = "Let's have fun with regular expressions!";
let unRegex = /.un/; // Change this line
let result = unRegex.test(exampleStr);
console.log(result)

// Match single character with multiple possibilities
// [] - this is called character classes
let bigStr = "big";
let bagStr = "bag";
let bugStr = "bug";
let bogStr = "bog";
pattern3 = /b[aiu]g/;
console.log('big', bigStr.match(pattern3));
console.log('bag', bagStr.match(pattern3));
console.log('bug', bugStr.match(pattern3));
console.log('bog', bogStr.match(pattern3));

let quoteSample = "Beware of bugs in the above code; I have only proved it correct, not tried it.";
let vowelRegex = /[aeiou]/gi; // Change this line
let result5 = quoteSample.match(vowelRegex); // Change this line
console.log('quoteSamples', result5);

// specifying range in a character set.
let quoteSample1 = "The quick brown fox jumps over the lazy dog.";
let alphabetRegex = /[a-z]/gi; // Change this line
let result6 = quoteSample1.match(alphabetRegex); // Change this line
console.log('quoteSamples1', result6);

