var arr_ = [6, 89, 3, 45];
console.log(arr_.length);

// the below line of code will return NaN as the fnction max expects comma seperated values and not an array.
console.log(Math.max(arr_));
console.log(Math.max(6, 89, 3, 45));

console.log('the maximum value in the array is: ', Math.max.apply(null, arr_));
console.log(...arr_);

const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
const arr2 = [...arr1];
console.log('The value of array2 is: ', arr2);




