// The function should return a new array containing the squares of only the positive integers (decimal numbers
// are not integers) when an array of real numbers is passed to it.

const squareList = arr => {
    const onlyPositiveIntegers = arr.filter(item => ((item > 0) && (item % 1 == 0)));
    arr = onlyPositiveIntegers.map(item => Math.pow(item, 2));
    return arr;
};

const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);