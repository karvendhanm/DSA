function chunkArrayInGroups(arr, size) {
    let _arr = [];
    let loopCount = Math.ceil(arr.length/size);
    for(let i=0; i<(loopCount); i++) {
        _arr.push(arr.slice(i*size, size+(i*size)));
    }
    return _arr;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2));