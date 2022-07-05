// second attempt
function translatePigLatin(str) {
    str = str.replace(/^([aeiou])(.*)/, '$1$2' + 'way');
    str = str.replace(/^([^aeiou]+)(.*)/, '$2$1'+'ay');
    return str;
}

console.log(translatePigLatin("eight"));

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