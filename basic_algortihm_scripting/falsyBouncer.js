function bouncer(arr) {
    let _arr = [];
    for(let i=0; i<arr.length; i++) {
        if(arr[i]) {
            _arr.push(arr[i]);
        }
    }
    return _arr;
}

console.log(bouncer([7, "ate", "", false, 9]));