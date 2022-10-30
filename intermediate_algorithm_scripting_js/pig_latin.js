// sixth attempt using recursion
function translatePigLatin(str, char_pos = 0) {
     return ['a', 'e', 'i', 'o', 'u'].includes(str[0]) ? str + (char_pos === 0 ? "way" : "ay")
         : char_pos === str.length ? str + "ay" : translatePigLatin(str.slice(1) + str[0], char_pos + 1);
}

console.log(translatePigLatin("rhythm"));

// // fifth attempt using recursion
// function translatePigLatin(str, char_pos = 0) {
//      return (['a', 'e', 'i', 'o', 'u'].includes(str[0]) && (char_pos === 0)) ? str + 'way'
//          : ((['a', 'e', 'i', 'o', 'u'].includes(str[0])) || (char_pos === str.length)) ? str + 'ay'
//              : translatePigLatin(str.slice(1) + str[0], char_pos + 1)
// }

// // fourth attempt
// function translatePigLatin(str) {
//     const _lst = ['a', 'e', 'i', 'o', 'u'];
//     return _lst.includes(str[0]) ? str + "way" : str.replace(/^([^aeiou]+)(.*)/, '$2$1ay')
// }

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