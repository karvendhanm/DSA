function uncurried(x, y) {
    return x + y;
}


console.log(uncurried(4, 5));


function curried(x) {
    return function (y) {
        return x + y;
    }
}

console.log(curried(4)(5));

const _curried = x => y => x + y;

console.log(_curried(1)(2));

const func = curried(4);
console.log(func(5));

// similarly, partial application can be described as applying a few arguments to a function at a time and returning
// another function that is applied to more arguments. Here's an example:

function impartial(x, y, z) {
    return x + y + z;
}

const partial = impartial.bind(this, 1, 2);
console.log(partial(10));


function add(x) {
    // Only change code below this line

    return function(y) {
        return function(z) {
            return x + y + z;
        }
    }

    // Only change code above this line
}

console.log(add(10)(20)(30));