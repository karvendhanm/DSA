let repeatStr = "row row row your boat";
let captureGrpPattern = /(\w+) \1 \1/;
console.log('Capture groups', repeatStr.match(captureGrpPattern));

let repeatNum = "42 42 42 42";
let reRegex = /^(\d+) \1 \1$/; // Change this line
let result = reRegex.test(repeatNum);
console.log(result);

