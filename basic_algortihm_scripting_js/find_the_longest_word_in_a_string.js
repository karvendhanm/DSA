function findLongestWordLength(str) {
    let words = str.split(" ");
    let _length = 0;
    for(let i=0; i<words.length; i++) {
        let wordLength = words[i].length;
        if(wordLength > _length) {
            _length = wordLength;
            str = words[i];
        }
    }
    return str.length;
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));