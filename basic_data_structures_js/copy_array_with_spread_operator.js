// ES6's new spread operator allows us to easily copy all of an array's elements, in order, with a simple and
// highly readable syntax. The spread syntax simply looks like this: ...

let thisArray = [true, true, false, undefined, null];
let thatArray = [...thisArray];

console.log('this array', thisArray);
console.log('that array', thatArray);

function copyMachine(arr, num) {
    let newArr = [];
    while (num >= 1) {
        // Only change code below this line
        newArr.push([...arr]);
        // Only change code above this line
        num--;
    }
    return newArr;
}

console.log(copyMachine([true, false, true], 2));