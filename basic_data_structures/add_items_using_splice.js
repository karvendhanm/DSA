const numbers = [9, 10, 11, 12, 12, 15];

const startIndex = 4;
const amountToDelete = 1;

numbers.splice(startIndex, amountToDelete, 13, 14);
console.log(numbers);

