// You will be provided with an initial array (the first argument in the destroyer function),
// followed by one or more arguments. Remove all elements from the initial array that are of the same
// value as these arguments.

// 4th attempt
function destroyer(arr) {
    const _lst = [arguments].reduce((accumulator, item) => {
        for(let key in item){
            if(key != 0) {
                accumulator.push(item[key]);
            }
        }
        return accumulator;
    }, [] )

    return arr.filter(item => _lst.indexOf(item) != -1 ? false : true)
}

console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3));

// 3rd attempt
// function destroyer(arr) {
//     const _lst = [];
//     for (let key in arguments){
//         if(key != 0){
//             _lst.push(arguments[key])
//         }
//     }
//
//     return arr.filter(item => _lst.indexOf(item) != -1 ? false : true)
// }

// 2nd attempt
// function destroyer(arr) {
//     const _lst = [];
//     for (let key in arguments){
//         if(key != 0){
//             _lst.push(arguments[key])
//         }
//     }
//
//     arr = arr.filter(item => {
//         if(_lst.indexOf(item) != -1) {
//             return false;
//         } else {
//             return true;
//         }
//     })
//
//     return arr;
// }

//  1st attempt
// function destroyer(arr) {
//     const _lst = [];
//     for (let key in arguments){
//         if(key != 0){
//             _lst.push(arguments[key])
//         }
//     }
//
//     for(let i=0; i<_lst.length; i++){
//         let _idx = arr.indexOf(_lst[i]);
//         while(_idx != -1) {
//             arr.splice(_idx, 1);
//             _idx = arr.indexOf(_lst[i]);
//         }
//     }
//
//     return arr;
//
// }