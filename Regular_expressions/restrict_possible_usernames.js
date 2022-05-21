let username = "AB1";
let userCheck = /^[a-zA-Z][a-zA-Z][a-zA-Z]*\d*$|^[a-zA-Z][a-zA-Z]$|^[a-zA-Z]\d\d+$/;
let result = userCheck.test(username);
console.log('login restrictions', result);

let whitespace = "Whitespace. Whitespace everywhere!";
let pattern = /\s/g;
console.log('whitespace everywhere', whitespace.match(pattern));

// searching for everything except whitespace
let sample = "Whitespace is important in separating words";
let non_white_space_pattern = /\S/g;
console.log('non-whitespace characters', sample.match(non_white_space_pattern));
