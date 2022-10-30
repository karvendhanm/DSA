const arr = [1, 2, 3, 4, 5, 6, 7, 8];

const [a, b] = arr;
console.log('the value of a and b is :', a, b);

// using commas to access elements at any index
const [i,j,,,,,k] = arr;
console.log('the value of i, j and k are: ', i, j, k);

// destructuring assignment.
let c = 6, d  = 8;

[c, d] = [d, c];

console.log('the value of c and d are: ', c, d);