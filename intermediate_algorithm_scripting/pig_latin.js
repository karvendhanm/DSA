// third attempt
function translatePigLatin(str) {
    str = str.replace(/^([aeiou])(.*)/, '$&way');
    str = str.replace(/^([^aeiou]+)(.*)/, '$2$1ay');
    return str;
}

console.log(translatePigLatin("eight"));

// // second attempt
// function translatePigLatin(str) {
//     str = str.replace(/^([aeiou])(.*)/, '$1$2' + 'way');
//     str = str.replace(/^([^aeiou]+)(.*)/, '$2$1'+'ay');
//     return str;
// }

// first attempt
// function translatePigLatin(str) {
//     const regexPattern = /^[aeiou]/;
//     if(regexPattern.test(str)) {
//         str = str + 'way';
//     } else {
//         str = str.replace(/([^aeiou]+)(.*)/, '$2$1'+'ay');
//     }
//
//     return str;
// }