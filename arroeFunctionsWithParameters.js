// writing arrow functions with parameters.

const myArrowFunc = (j) => {
    return j*=4;
}

// syntactic sugar of the function above.
const myArrowFunc1 = (k) => k*=4;

// even more syntatic sugar to go around.
const myArrowFunc2 = item => item *= 6;

console.log('the value of myArrowFunc is: ', myArrowFunc(5));
console.log('the value of myArrowFunc1 is: ', myArrowFunc1(20));
console.log('the value of myArrowFunc2 is: ', myArrowFunc2(60));

let multiplier = (item, multi) => item*multi;
console.log('the value of the multiplier is: ', multiplier(4, 5));

const arr1 = [1, 2];
const arr2 = [3, 4, 5];

console.log('array concatination value is:', arr1.concat(arr2));