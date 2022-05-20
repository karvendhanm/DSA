let quoteSample = "Blueberry 3.141592653s are delicious.";
let myRegex = /[a-z0-9]/gi; // Change this line
let result = quoteSample.match(myRegex); // Change this line
console.log(result);

// Matching characters not specified
// negated character sets

let str_ = 'learning is fun, consistently doing it is even more fun';
let pattern = /[^aeiou]/gi;
console.log('negated character sets', str_.match(pattern));

//  Match characters that occur one or more times.
let str_mississippi = 'Mississippi';
let pattern_str = /s+/g;
console.log('s in mississippi', str_mississippi.match(pattern_str));
console.log('s in mississippi test', pattern_str.test(str_mississippi));

// Match characters that occur zero or more times.
let soccerWord = "gooooooooal!";
let gPhrase = "gut feeling";
let oPhrase = "over the moon";
let pattern_mde = /go*/;
console.log(soccerWord.match(pattern_mde));
console.log(gPhrase.match(pattern_mde));
console.log(oPhrase.match(pattern_mde));

























