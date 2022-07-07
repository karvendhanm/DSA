// first attempt
function myReplace(str, before, after) {
    const regex_pattern = new RegExp(before, 'i');
    if(regex_pattern.test(str)) {
        let word = str.match(regex_pattern)[0];
        if((word.charAt(0) === word.charAt(0).toUpperCase()) !== (after.charAt(0) === after.charAt(0).toUpperCase())){
            if (after.charAt(0) === after.charAt(0).toUpperCase()) {
                after = after.charAt(0).toLowerCase() + after.slice(1);
            } else {
                after = after.charAt(0).toUpperCase() + after.slice(1);
            }
        }
    }
    return str.replaceAll(before, after);
}

console.log(myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped"));
console.log(myReplace("Let us go to the store", "store", "mall"));
console.log(myReplace("He is Sleeping on the couch", "Sleeping", "sitting"));
console.log(myReplace("I think we should look up there", "up", "Down"));
console.log(myReplace("This has a spellngi error", "spellngi", "spelling"));
console.log(myReplace("His name is Tom", "Tom", "john"));
console.log(myReplace("Let us get back to more Coding", "Coding", "algorithms"));