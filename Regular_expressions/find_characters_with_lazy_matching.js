_str1 = 'titanic';
greedyPattern = /t[a-z]*i/;
lazyPattern = /t[a-z]*?i/;
console.log('greedy pattern', _str1.match(greedyPattern));
console.log('lazy pattern', _str1.match(lazyPattern));

let text = "<h1>Winter is coming</h1>";
let myRegex = /<h.*?>/; // Change this line
let result = text.match(myRegex);
console.log('HTML', result);




