// fourth attempt
function translatePigLatin(str) {
    const _lst = ['a', 'e', 'i', 'o', 'u'];
    return _lst.includes(str[0]) ? str + "way" : str.replace(/^([^aeiou]+)(.*)/, '$2$1ay')
}

console.log(translatePigLatin("eight"));

// // third attempt
// function translatePigLatin(str) {
//     str = str.replace(/^([aeiou])(.*)/, '$&way');
//     str = str.replace(/^([^aeiou]+)(.*)/, '$2$1ay');
//     return str;
// }

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