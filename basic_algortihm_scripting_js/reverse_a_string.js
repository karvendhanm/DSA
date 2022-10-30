function reverseString(str) {
    let arr = str.split("");
    arr.reverse();
    str = arr.join("");
    return str;
}

console.log(reverseString("Greetings from Earth"));