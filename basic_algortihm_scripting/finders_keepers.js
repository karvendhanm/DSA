function findElement(arr, func) {
    let num = undefined;
    for(let i=0; i<arr.length; i++) {
        if(func(arr[i])) {
            return arr[i];
        }
    }
    return num;
}

let j = findElement([1, 3, 5, 9], num => num % 2 === 0);
console.log(j);