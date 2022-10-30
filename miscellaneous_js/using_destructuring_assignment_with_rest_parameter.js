function make(...args) {
    console.log('the length of the parameters is: ', args.length);
}

make(1, 2, 3, 4);

const arr1 = [1, 2, 3, 4, 5, 6, 7];
const [a, b, c, ...arr] = arr1;

console.log(a, b, c);
console.log(arr);