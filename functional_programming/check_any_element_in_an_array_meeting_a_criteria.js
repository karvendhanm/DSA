const numbers = [10, 50, 8, 220, 110, 11];

console.log(numbers.some((item) => {
    return item < 10;
}))

function checkPositive(arr) {
    // Only change code below this line

    return arr.some(function(item) {
        return item > 1;
    });

    // Only change code above this line
}

console.log(checkPositive([1, 2, 3, -4, 5]));