function mutation(arr) {
    for(let k=0; k<arr.length; k++){
        arr[k] = arr[k].toLowerCase();
    }

    let flag = false;
    let firstWord = arr[0].split("");
    let secondWord = arr[1].split("");

    let _idx = 0;
    for(let i=0; i<secondWord.length; i++) {
        if(firstWord.includes(secondWord[i])) {
            _idx += 1;
        }
    }

    if(_idx === secondWord.length) {flag = true;}

    return flag;
}

console.log(mutation(["hello", "hey"]));