function getIndexToIns(arr, num) {
    arr.sort(function (a, b) {  return a - b;});
    let _idx = 0;
    for(let i=0; i<arr.length; i++) {
        if(arr[i] >= num) {
            _idx = i;
            break;
        } else if((arr[i] < num) && (i === (arr.length - 1))) {
            _idx = arr.length;
        }
    }
    return _idx;
}

console.log(getIndexToIns([2, 5, 10], 15));