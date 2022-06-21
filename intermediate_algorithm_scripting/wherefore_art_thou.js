// 2nd attempt
function whatIsInAName(collection, source) {
    return collection.filter(item => {
        let k = 0;
        for(let key in source) {
            if ((item.hasOwnProperty(key)) && (item[key] === source[key])){
                k += 1;
                if(k === Object.keys(source).length) {
                    return true;
                }
            }
        }
    });
}

console.log(whatIsInAName([{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }], { "apple": 1 }));

// 1st attempt
// function whatIsInAName(collection, source) {
//     const arr = [];
//     for(let i=0; i<collection.length; i++) {
//         let sourceKeyLength = Object.keys(source).length;
//         let k = 0;
//         for(let key in source){
//             if(collection[i].hasOwnProperty(key)) {
//
//                 if(collection[i][key] === source[key]) {
//                     k += 1;
//                     if(k === sourceKeyLength){
//                         arr.push(collection[i]);
//                     }
//                 }
//             }
//         }
//     }
//     return arr;
// }