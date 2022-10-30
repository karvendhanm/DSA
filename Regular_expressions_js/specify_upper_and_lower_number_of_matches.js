// specify upper and lower number of matches

// quantity specifiers.
let A4 = "aaaah";
let A2 = "aah";
let pattern = /a{3,5}h/;
console.log(A4.match(pattern));
console.log(A2.match(pattern));

// Specify only the lower number of matches
let haStr = "Hazzzzah";
let haRegex = /Haz{4,}ah/; // Change this line
let result = haRegex.test(haStr);

console.log("there is a div here");

// Specify exact number of matches
let A5 = "haaaah";
let A3 = "haaah";
let A100 = "h" + "a".repeat(100) + "h";
let pattern_quantity_specifiers = /ha{3}h/;
console.log(A5.match(pattern_quantity_specifiers));
console.log(A3.match(pattern_quantity_specifiers));
console.log(A100.match(pattern_quantity_specifiers));
