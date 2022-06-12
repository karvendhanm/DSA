// The global variable
const s = [23, 65, 98, 5];

Array.prototype.myMap = function(callback) {
    const newArray = [];
    // Only change code below this line

    // for(let i = 0; i < s.length; i++) {
    //     newArray.push(callback(s[i]));
    // }

    s.forEach((item, index) => {
        newArray.push(callback(item));
    })

    // Only change code above this line
    return newArray;
};

const new_s = s.myMap(item  => item * 2);

console.log(new_s);

const avengers = ['thor', 'captain america', 'hulk'];
avengers.forEach((item, index) => {
    console.log(index, item)
})

