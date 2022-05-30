function frankenSplice(arr1, arr2, n) {
    let _arr = arr2.slice(0);
    _arr.splice(n, 0, ...arr1);
    return _arr;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);