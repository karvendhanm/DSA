const globalArray = [5, 6, 3, 2, 9];

function nonMutatingSort(arr) {
    // Only change code below this line

    const arr1 = [...arr];
    // const arr1 = arr.slice();
    // const arr1 = [].concat(arr);
    return arr1.sort(function(a, b) {
        return a === b ? 0 : a > b ? 1 : -1;
    });

    // Only change code above this line
}

nonMutatingSort(globalArray);