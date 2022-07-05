// second attempt
function spinalCase(str) {
//  Spinal tape case:
    const regex_pattern0 = /(?<!^)([A-Z])/g;
    const regex_pattern1 = /[^a-zA-Z]+/g;
    str = str.replace(regex_pattern0, '*\$1');
    str = str.replace(regex_pattern1, '-');
    str = str.toLowerCase();
    return str;

}

console.log(spinalCase('This Is Spinal Tap'));
console.log(spinalCase('thisIsSpinalTap'));
console.log(spinalCase('The_Andy_Griffith_Show'));
console.log(spinalCase('Teletubbies say Eh-oh'));
console.log(spinalCase('AllThe-small Things'));

// first attempt
// function spinalCase(str) {
// //  Spinal tape case:
//
//     const regex_pattern0 = /[^a-zA-Z]/g;
//     const regex_pattern1 = /(?<!^)([A-Z])/g;
//     str = str.replace(regex_pattern0, '*');
//     str = str.replace(regex_pattern1, '*\$1');
//     str = str.toLowerCase();
//     str = str.replace(/\*+/g, "-");
//     return str;
//
// }
