let firstString = "Ricky is first and can be found";
let firstRegex = /^Ricky/;
console.log('caret smbol', firstString.match(firstRegex));
let notFirst = "You can't find Ricky now.";
console.log('Cannot find ricky now', firstRegex.test(notFirst));

let theEnding = "This is a never ending story";
let storyRegex = /story$/;
storyRegex.test(theEnding);
let noEnding = "Sometimes a story will have to end";
storyRegex.test(noEnding);

// Matching all letters and numbers
// shorthand character classes
// shorthand character classes

let patternw = /\w+/;
let patternlong = /[A-Za-z0-9_]+/;
let numbers = "42";
let var_names = "important_var";
console.log(patternw.test(numbers));
console.log(patternw.test(var_names));
console.log(patternlong.test(numbers));
console.log(patternlong.test(var_names));

let quoteSample = "The five boxing wizards jump quickly.";
let patt = /\w+/g;
console.log(quoteSample.match(patt).length);

// Match everything but letters and numbers
let quoteSample2 = "The five boxing wizards jump quickly.";
let patt_sample = /\W/g;
console.log(quoteSample2.match(patt_sample));

let shorthand = /\W/;
let numbers1 = "42%";
let sentence = "Coding!";
console.log(numbers1.match(shorthand));
console.log(sentence.match(shorthand));










