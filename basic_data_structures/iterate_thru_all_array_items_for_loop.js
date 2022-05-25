function greater_than_ten(arr) {
    let newarr = [];
    for(let i=0; i<arr.length; i++) {
        if(arr[i] > 10) {
            newarr.push(arr[i]);
        }
    }

    return newarr;
}

console.log(greater_than_ten([2, 12, 8, 14, 80, 0, 1]));

// We have defined a function, filteredArray, which takes arr, a nested array, and elem as arguments, and
// returns a new array. elem represents an element that may or may not be present on one or more of the arrays
// nested within arr. Modify the function, using a for loop, to return a filtered version of the passed array such
// that any array nested within arr containing elem has been removed.

function filteredArray(arr, elem) {
    let newArr = [];
    // Only change code below this line
    for(let j = 0; j < arr.length; j++) {
        if(arr[j].indexOf(elem) == -1){
            newArr.push(arr[j]);
        }
    }

    // Only change code above this line
    return newArr;
}

console.log(filteredArray([[10, 8, 3], [14, 6, 23], [3, 18, 6]], 18));