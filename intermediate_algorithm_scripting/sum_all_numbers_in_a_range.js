function sumAll(arr) {
    let sorted_arr = [...arr];
    sorted_arr = sorted_arr.sort(function(a, b) {
        return a - b;
    });

    let _lst = 0;
    for(let i = sorted_arr[0]; i <= sorted_arr[1]; i++) {
        _lst += i;
    }

    return _lst;
}

console.log(sumAll([1, 4]));