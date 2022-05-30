function chunkArrayInGroups(arr, size) {
    let _arr = [];
    let loopCount = Math.floor(arr.length/size);
    let remainder = Math.floor(arr.length%size);
    if(remainder) {remainder = 1}
    for(let i=0; i<(loopCount + remainder); i++) {
        _arr.push(arr.slice(0+(i*size), size+(i*size)));
    }
    return _arr;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2));