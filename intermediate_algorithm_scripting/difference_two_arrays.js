function diffArray(arr1, arr2) {

    const arr = arr1.concat(arr2);

    const newArr = [];
    arr.filter(item => {
        if(!(arr1.includes(item)) || !(arr2.includes(item))){
            newArr.push(item);
        }
    })

    return newArr;
}

console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]));

// Symmetric difference between two arrays, 1st attempt
// function diffArray(arr1, arr2) {
//
//     const arr = arr1.concat(arr2);
//
//     let counter = {};
//     arr.forEach(item => {
//         counter[item] = (counter[item] || 0) +  1;
//         return counter;
//     });
//
//     const newArr = [];
//     for (let key in counter){
//         if (counter[key] === 1) {
//             newArr.push(parseInt(key) || key);
//         }
//     }
//
//     return newArr;
// }




