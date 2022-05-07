// scope of the var decleration of a variable
var numArray = [];
for(var i=0; i<3; i++) {
    numArray.push(i);
}

console.log(numArray);
// i is accessed in the below line. So i has a global scope.
console.log(i);

let numArraylet = [];
for(let j=0; j<3; j++) {
    numArraylet.push(j);
}

console.log(numArraylet);
// The below line of code can't be executed as j has been initialized as let.
// console.log(j);

var printNumberTwo;
for(var k=0; k<3; k++) {
    if (k === 2) {
        printNumberTwo = function() {
            return k;
        };
    }
}

console.log("the number printed with var keyword is: ", printNumberTwo())


let printNumberTwo_;
for(let l=0; l<3; l++) {
    if (l === 2) {
        printNumberTwo_ = function() {
            return l;
        };
    }
}

console.log("the number printed with let keyword is: ", printNumberTwo_())


for(let m=0; m<3; m++) {
    var inside_ = 85;
}

console.log("The inside_ is: ", inside_);

// clear illustration of let keyword
let p = 0;
// the below line is not valid.
// let p = 1;

function checkScope() {
    let i = 'function scope';
    if(true) {
        // console.log('immediately after entering the if statement', i);
        let i='block scope'
        console.log('just about to exit the if statement:', i);
    }
    return i;
}

console.log(checkScope());




