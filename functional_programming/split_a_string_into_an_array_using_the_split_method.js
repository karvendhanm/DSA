const _str = "Hello World";
console.log(_str.split(" "));

const otherString = "How9are7you2today";
console.log(otherString.split(/\d/));


function splitify(str) {
    // Only change code below this line
    const pattern = /[^a-zA-z\s]/g;
    return str.replace(pattern, " ").split(" ");
    // Only change code above this line
}

console.log(splitify("Hello World,I-am code"));