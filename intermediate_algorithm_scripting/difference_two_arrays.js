function diffArray(arr1, arr2) {

    const arr = arr1.concat(arr2);

    let counter = {};
    arr.forEach(item => {
        counter[item] = (counter[item] || 0) +  1;
        return counter;
    });

    const newArr = [];
    for (let key in counter){
        if (counter[key] === 1) {
            newArr.push(parseInt(key) || key);
        }
    }

    return newArr;
}

console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]));




