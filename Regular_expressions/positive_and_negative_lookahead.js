// Positive and negative lookahead
let quit = "qu";
let noquit = "qt";
let pattern1 = /q(?=u)/;
let pattern2 = /q(?!u)/;
console.log(quit.match(pattern1));
console.log(quit.match(pattern2));
console.log(noquit.match(pattern1));
console.log(noquit.match(pattern2));

// A more practical use of lookaheads is to check two or more patterns in one string.
// Here is a (naively) simple password checker that looks for between 3 and 6 characters and at least one number:
let password = "abc773";
password_pattern = /(?=\w{3,6})(?=\D*\d\D*)/;
console.log('password checker', password.match(password_pattern));

// Use lookaheads in the pwRegex to match passwords that are greater than 5 characters long,
// and have two consecutive digits.

let sampleWord = "astronaut";
let pwRegex = /(?=\S{6,})(?=\D*\d{2,}\D*)/; // Change this line
let result = pwRegex.test(sampleWord);
