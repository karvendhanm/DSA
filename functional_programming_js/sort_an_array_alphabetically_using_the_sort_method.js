function ascending_order(arr) {
    const _ret1 = arr.sort(function (a, b) {
        const _ret2 = a - b;
        return _ret2;
    });
    return _ret1
}

console.log(ascending_order([1, 5, 2, 4, 3]))

function reverseAlpha(arr) {
    return arr.sort(function(a, b) {
        return a === b ? 0 : a > b ? -1 : 1;
    });
}

console.log(reverseAlpha(['l', 'h', 'z', 'b', 's']));