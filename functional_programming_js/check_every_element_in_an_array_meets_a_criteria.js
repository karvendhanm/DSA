const numbers = [1, 4, 6, 0, 10, 11]

console.log(numbers.every(item => {return item < 10}));
// console.log(numbers.every(function(item) {
//     return item < 10;
// }));

function checkPositive(arr) {
    // Only change code below this line

    return arr.every(function(item) {
        return item > 0;
    })

    // Only change code above this line
}

console.log(checkPositive([1, 2, 3, -4, 5]));