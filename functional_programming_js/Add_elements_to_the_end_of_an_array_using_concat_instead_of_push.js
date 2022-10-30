// Functional programming is all about creating and using non-mutating functions.

// The last challenge introduced the concat method as a way to combine arrays into a new one without mutating the
// original arrays. Compare concat to the push method. push adds an item to the end of the same array it is called on,
// which mutates that array. Here's an example:

function nonMutatingPush(original, newItem) {
    // Only change code below this line
    return original.concat(newItem);

    // Only change code above this line
}

const first = [1, 2, 3];
const second = [4, 5];
const finalArray = nonMutatingPush(first, second);

console.log(finalArray);